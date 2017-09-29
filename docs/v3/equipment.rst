Using Equipment module
######################

Assuming that you have Client Factory instantiated (see :ref:`How to Instantiate Client Factory <client-factory>`) at **client** variable, in order to access methods relative to Equipment module you need to call create_api_equipment() at **client**.

Example:

.. code-block:: python

   eqpt_module = client.create_api_equipment()

For more information, please look GloboNetworkAPI documentation.

GET
***

The List of fields available at Equipment module is:

    * id
    * name
    * maintenance
    * equipment_type
    * model
    * ipv4
    * ipv6
    * environments
    * groups

Obtain List of Equipments through id's
======================================

Here you need to call get() method at eqpt_module.

You can pass up to 5 parameters:
    * **ids**: List containing identifiers of equipments.
    * **include**: Array containing fields to include on response.
    * **exclude**: Array containing fields to exclude on response.
    * **fields**: Array containing fields to override default fields.
    * **kind**: string where you can choose between "basic" or "details".

The response will be a dict with a list of Equipments.

Examples:

.. code-block:: python

    epqts = eqpt_module.get(ids=[1, 2, 3])

.. code-block:: python

    epqts = eqpt_module.get(ids=[1, 2, 3],
                            include=['name', 'maintenance'],
                            exclude=['id'],
                            kind='basic')

.. code-block:: python

    epqts = eqpt_module.get(ids=[1, 2, 3],
                            fields=['id', 'name', 'model'])

Obtain List of Equipments through extended search
=================================================

Here you need to call search() method at eqpt_module.

You can pass up to 5 parameters:
    * **search**: Dict containing QuerySets to find equipments.
    * **include**: Array containing fields to include on response.
    * **exclude**: Array containing fields to exclude on response.
    * **fields**: Array containing fields to override default fields.
    * **kind**: string where you can choose between "basic" or "details".

The response will be a dict with a list of Equipments.

Example:

.. code-block:: python

    search = {
        'extends_search': [{
            'maintenance': false,
            'tipo_equipamento': 1
        }],
        'start_record': 0,
        'custom_search': '',
        'end_record': 25,
        'asorting_cols': [],
        'searchable_columns': []}
    fields = ['id', 'name', 'model']

    epqts = eqpt_module.search(search=search, fields=fields)

POST
****

The List of fields available for create an Equipment is:

    * environments
        * id
        * is_router
        * is_controller
    * equipment_type - **Mandatory**
    * groups
        * id
    * ipv4
        * id
    * ipv6
        * id
    * maintenance - **Mandatory**
    * model - **Mandatory**
    * name - **Mandatory**

Create List of Equipments
=========================

Here you need to call create() method at eqpt_module.

You need to pass 1 parameter:
    * **equipments**: List containing equipments that you want to create.

Example:

.. code-block:: python

    eqpts_to_create = [
        {
            "name": "Eqpt-1",
            "maintenance": False,
            "equipment_type": 8,
            "model": 3,
            "environments": [
                {
                    "id": 1,
                    "is_router": True,
                    "is_controller": False
                },
                {
                    "id": 2,
                    "is_router": False,
                    "is_controller": False
                }
            ],
            "ipv4": [1, 2]
        },
        {
            "name": "Eqpt-2",
            "maintenance": False,
            "equipment_type": 9,
            "model": 3,
            "ipv6": [1, 2],
            "groups": [
                {
                    "id": 1
                },
                {
                    "id": 2
                }
            ]
        }
    ]

    eqpt_module.create(equipments=eqpts_to_create)


PUT
***

The List of fields available for update an Equipment is:

    * id - **Mandatory**
    * environments
        * id
        * is_router
        * is_controller
    * equipment_type - **Mandatory**
    * groups
        * id
    * ipv4
        * id
    * ipv6
        * id
    * maintenance - **Mandatory**
    * model - **Mandatory**
    * name - **Mandatory**

Update List of Equipments
=========================

Here you need to call update() method at eqpt_module.

You need to pass 1 parameter:
    * **equipments**: List containing equipments that you want to update.

Example:

.. code-block:: python

    eqpts_to_update = [
        {
            "id": 1,
            "name": "Eqpt-1-Updated",
            "maintenance": False,
            "equipment_type": 2,
            "model": 2,
            "environments": [
                {
                    "id": 2,
                    "is_router": True,
                    "is_controller": False
                }
            ],
            "ipv4": [3, 5, 7]

        },
        {
            "id": 2,
            "name": "Eqpt-2-Updated",
            "maintenance": False,
            "equipment_type": 7,
            "model": 2,
            "ipv6": [1, 2],
            "groups": [
                {
                    "id": 2
                },
                {
                    "id": 3
                }
            ]
        }
    ]

    eqpt_module.update(equipments=eqpts_to_update)

DELETE
******

Delete List of Equipments
=========================

Here you need to call delete() method at eqpt_module.

You need to pass 1 parameter:
    * **ids**: List containing identifiers of equipments that you want to delete.

Example:

.. code-block:: python

    eqpt_module.delete(ids=[1, 2, 3])

