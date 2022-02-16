# rugviz

Rugviz is a Django application that provides an online ordering platform for carpets.
Its key features are:-
* customers can register themselves on this platform either as individual buyers or corporate customer.
* both types of buyers can place a purchase order for carpets.
* purchase order should lead to email being placed to the purchasing and the selling party.
* inventory objects can be created and managed by importing the excel packing sheets in the management console.
* inventory objects can also be optionally created by adding new images of carpets in the new_images folder in the media folder.
* basic views:
    * list - list of all carpets
    * detail - detail of a carpet/collection/collection in design
    * cart - cart which can be ordered
    * Django admin - admin panel where the objects of the model can be viewed there,
                     along with performing key actions like importing/exporting packing sheet

### Deployment
We use Heroku for the deployments of this project.
* Any commit on the `prod` branch will [automatically be deployed to live](https://dashboard.heroku.com/apps/rugviz).
* Any PRs on the `main` branch will trigger a [pipeline](https://dashboard.heroku.com/pipelines/4d975311-c770-4054-a8bd-87ff1bb27eca) that will create a reviewer deployment
    that can be used by all the developers to view and assess their changes better.
