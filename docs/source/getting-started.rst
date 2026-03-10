***************
Getting started
***************

This tutorial walks you through how to make a simple package. It will show you how to add the necessary files and structure to create the package, and how to upload it to github.

.. tip::

   If you have trouble with this tutorial, please open an issue on
   GitHub. We'll do our best to help you!


Requirements
------------

To start making a package you will need a good code editor. In this tutorial we will be using visual `studio code`_

.. _visual studio code: https://code.visualstudio.com

got it installed? great! open a folder of your choosing and lets get to work

File structure
--------------
The file structure for a project is pretty simple but first you have to choose a namespace.
A namespace is usually the name of the mod your adding stuff for/to if your unsure of which namespace to use or arnt adding stuff to or for a specific mod just set it to kpm.
You can have multiple namespaces in a package.

Create this file structure:

.. code-block:: text

    project_folder
    ├── registry.toml
    └── server_scripts
        └── namespace
            └── recipes.js

Registry.toml
--------------
The registry.toml file is the most important file in a project. it tells tfg-kpm what classes to register and the name of the package.
by default a registry.toml should look like this.

.. code-block:: toml

    [tfg-kpm.main]
    name = "my_package" # replace with your package name

    [tfg-kpm.package]
    recipes = []
    itemtags = []
    blocktags = []
    fluidtags = []

Creating a recipe
-----------------
As a example im going to show you how to add a recipe that lets you craft craft diamond powder back into diamond dust. (i have no ideas bear with me)

Lets start with making a class.

your class name can be anything but for organization its usually something like registernamespaceRecipes so lets start with that.
for this example im using the kpm namespace.

Paste this into your recipes.js file. (you can replace Kpm with your namespace)

.. code-block:: javascript

    // priority: 0
    "use strict";

    const registerKpmRecipes = (event) => {

    }

Now lets add the recipe

.. code-block:: javascript

    // priority: 0
    "use strict";

    const registerKpmRecipes = (event) => {
        event.shapeless(
            Item.of('gtceu:diamond_dust', 1), // arg 1: output
            [
                '4x tfc:powder/diamond',  // arg 2: the array of inputs
            ]
        )
    }

Now we must register it in registry.toml, add your class to the recipes array like this.

.. code-block:: toml

    recipes = ["registerKpmRecipes"]

and your done!

Publishing to github
--------------------

Your almost there you just need to publish your package to github.
Go to the source control tab on your sidebar and click publish to github.
