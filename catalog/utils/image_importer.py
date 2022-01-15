

from django.conf import settings
import os
# Register your models here.
from catalog.models import *
from parse import *
from django.contrib import messages
from collections import OrderedDict
from django.core.files import File
from pathlib import Path

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
        if model_obj.image_file:
            # TODO: should we delete the file here?
            self.model_admin.message_user(self.request, "Image already exists for :" + file_path + ". File not deleted.", messages.WARNING)
            # os.remove(file_path)
        else:
            file_path = Path(file_path)
            f = open(file_path, 'rb')
            model_obj.image_file.save(os.path.basename(file_path), File(f))
            model_obj.save()
            os.remove(file_path)
            self.model_admin.message_user(self.request, "Image added for :" + file_path + ". Deleteing this file.", messages.SUCCESS)

    def handle_file(self, file_path, file_name):
        # retrieve collection, design, color, size by parsing file name
        model_field_values = self.parse_filename(file_name)
        try:
            model_field_values['design__name'] = str(model_field_values['design__name'])
            qs = DesignInColor.objects.filter(design__name__startswith=model_field_values['design__name'], color__primary_color=model_field_values['color__primary_color'], color__texture_color=model_field_values['color__texture_color'])
            if qs.count()>0:
                self.save_image_in_model(qs[0], file_path)
            else:
                # found design in color in carpet image that is not in the model.
                # create new object then save the image there.
                image_collection_name = self.search_collection()
                image_design_name = model_field_values['design__name']
                # TODO: I think that the design variation logic should be created in the design model
                # for now in this else all designs are unique with no variation.
                image_collection_obj, _ = Collection.objects.get_or_create(name=image_collection_name)
                design_obj, _ = Design.objects.get_or_create(name=image_design_name,
                                                             collection=image_collection_obj)
                color_obj, _  = Color.objects.get_or_create(primary_color=model_field_values["color__primary_color"],
                                                            texture_color=model_field_values["color__texture_color"])
                design_in_color_obj = DesignInColor.objects.create(design=design_obj,
                                                                   color=color_obj)
                self.save_image_in_model(design_in_color_obj, file_path)

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
        # NOTE: I think that storing stack is a bit confusing.
        # IMHO it would be better if we just passed the complete file path here and have the seach as a static function.
        # the same stack can be easily create by spliting the file path.
        # for mocking purpose I am return "Alvita"
        return "ALVITA"

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