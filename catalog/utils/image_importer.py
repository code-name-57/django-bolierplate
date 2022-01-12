

from django.conf import settings
import os
# Register your models here.
from catalog.models import *
from parse import *
from django.contrib import messages
from collections import OrderedDict
from django.core.files import File

class ImageImporter:
    def __init__(self, request, queryset, model_admin):
        self.request = request
        self.queryset = queryset
        self.model_admin = model_admin
        self.new_images_path = os.path.join(settings.MEDIA_ROOT, "new_images")

        # Stack to keep track of path from root directory to file
        self.stack = []

        # Call recursive function
        self.import_new_images(self.new_images_path)

    def import_new_images(self, path):
        files = os.listdir(path)
        for file in files:
            new_path = os.path.join(path, file)
            if os.path.isdir(new_path):
                # moving into a directory
                self.stack.append(file)
                self.model_admin.message_user(self.request, " folder :" + new_path, messages.SUCCESS)
                self.import_new_images(new_path)
                
                # moved out of directory
                self.stack.pop()
            else:
                self.handle_file(new_path, file)

    def save_image_in_model(self, model_obj, file_path):
        breakpoint()
        if model_obj.image_file:
            self.model_admin.message_user(self.request, "Image already exists for ")
            f = open(file_path, 'r')
            model_obj.image_file = File(f)
            model_obj.save()
        else:
            f = open(file_path, 'r')
            model_obj.image_file = File(f)
            model_obj.save()
            # delete image from current path
            # paste image in catalog
            # save catalog path as model_obj.image_path
            # model_
        pass

    def handle_file(self, file_path, file_name):
        # retrieve collection, design, color, size by parsing file name
        model_field_values = self.parse_filename(file_name)
        print(model_field_values, file_name)
        # (**model_field_values)
        try:
            qs = DesignInColor.objects.filter(design__name__startswith=model_field_values['design__name'], color__primary_color=model_field_values['color__primary_color'], color__texture_color=model_field_values['color__texture_color'])
            if qs.count()>0:
                self.model_admin.message_user(self.request, " file :" + file_path + "model : " + str(qs[0]), messages.SUCCESS)
                self.save_image_in_model(qs[0], file_path)
        except KeyError as e:
            self.model_admin.message_user(self.request, "error file name: " + file_name, messages.ERROR)
        #    / pass
        # qs = DesignInColor.objects.filter(**model_field_values)
        # breakpoint()
        # if file name does not contain all details, then look for it in self.stack which is path of file from root directory
        # if model_field_values['design__collection__name'] is None:
        #     model_field_values['design__collection__name'] = self.search_collection()
        # if design is None:
        #     design = self.search_design()
        # if color is None:
        #     color = self.search_color()
        # if size is None:
        #     size = self.search_size()
        
        # if size is None:
        #     # No size found in filename of directories, so try adding image to DesignColor model
        #     self.add_design_color_image(file_path, collection, design, color)
        # else:
        #     # There is size either in filename or dorectory, so try adding image Carpet model
        #     self.add_carpet_image(file_path, collection, design, color, size)

        # self.model_admin.message_user(self.request, " file :" + file_path, messages.SUCCESS)


    def parse_filename(self, file_name):
        # Alvita 2120 Blue Cream 7x9.jpg (@ /new_images/)
        # Blue Cream.jpg (@ /new_images/alvita/2120/)
        file_name = " ".join(file_name.split())
        output = dict()
        list_parse = OrderedDict()
        list_parse["{:d} {:w} {:w}.{:w}"] = \
            ['design__name', 'color__primary_color', 'color__texture_color'] # 2120 Blue Cream.jpg (@ /new_images/alvita/)
        list_parse["{:d}{:w} {:w} {:w}.{:w}"] = \
            ["design__name", "variation", "color__primary_color", "color__texture_color"]   # 2120A Blue Cream.jpg (@ /new_images/alvita/)
        list_parse["{:w} {:d} {:w} {:w}.{:w}"] = \
            ['collection', 'design__name', 'color__primary_color', 'color__texture_color'] # Alvita 2120 Blue Cream.jpg (@ /new_images/)
        list_parse["{:w} {:d}{:w} {:w} {:w}.{:w}"] = \
            ["collection", "design__name", "variation", "color__primary_color", "color__texture_color"] # Alvita 2120B Blue Cream.jpg (@ /new_images/)

        for key, value in list_parse.items():
            prs = parse(key, file_name, case_sensitive=False)
            if prs:
                for i, x in enumerate(value):
                    output[x] = prs[i]
                break
        return output
        
    def search_collection(self):
        # TODO search collection name in stack
        return None

    def search_color(self):
        # TODO search color name in stack
        return None

    def search_design(self):
        # TODO search design nuber in stack
        return None

    def search_size(self):
        # TODO search size in stack
        return None

    def add_design_color_image(self, image_path, collection, design, color):
        # TODO search designINCOlor model for these value, add image if not already there
        pass

    def add_carpet_image(self, image_path, collection, design, color, size):
        # TODO search carpet model for these value, add image if not already there
        pass