Using Environment Vip module
############################

Assuming that you have Client Factory instantiated (see :ref:`How to Instantiate Client Factory <client-factory>`) at **client** variable, in order to access methods relative to Environment Vip module you need to call create_api_environment_vip() at **client**.

Example:

.. code-block:: python

   envvip_module = client.create_api_environment_vip()

For more information, please look GloboNetworkAPI documentation.

GET
***

The List of fields available at Environment Vip module is:

    * id
    * finalidade_txt
    * cliente_txt
    * ambiente_p44_txt
    * description
    * name
    * conf
    * optionsvip
    * environments

Obtain List of Environment Vip through id's
===========================================

Here you need to call get() method at envvip_module.

You can pass up to 5 parameters:
    * **ids**: List containing identifiers of environment vips.
    * **include**: Array containing fields to include on response.
    * **exclude**: Array containing fields to exclude on response.
    * **fields**: Array containing fields to override default fields.
    * **kind**: string where you can choose between "basic" or "details".

The response will be a dict with a list of Environment Vips.

Examples:

.. code-block:: python

    env_vips = envvip_module.get(ids=[1, 2, 3])

.. code-block:: python

    env_vips = envvip_module.get(ids=[1, 2, 3],
                                 include=['name', 'finalidade_txt'],
                                 exclude=['id'],
                                 kind='details')

.. code-block:: python

    env_vips = envvip_module.get(ids=[1, 2, 3],
                                 fields=['id', 'ambiente_p44_txt', 'conf'])

Obtain List of Environment Vips through extended search
=======================================================

Here you need to call search() method at envvip_module.

You can pass up to 5 parameters:
    * **search**: Dict containing QuerySets to find environment vips.
    * **include**: Array containing fields to include on response.
    * **exclude**: Array containing fields to exclude on response.
    * **fields**: Array containing fields to override default fields.
    * **kind**: string where you can choose between "basic" or "details".

The response will be a dict with a list of Environment Vips.

Example:

.. code-block:: python

    search = {
        'extends_search': [{
            'description__icontains': 'EnvVip-Test',
        }],
        'start_record': 0,
        'custom_search': '',
        'end_record': 25,
        'asorting_cols': [],
        'searchable_columns': []}
    fields = ['id', 'name']

    env_vips = envvip_module.search(search=search, fields=fields)

POST
****

The List of fields available for create an Environment Vip is:

    * finalidade_txt - **Mandatory**
    * cliente_txt - **Mandatory**
    * ambiente_p44_txt - **Mandatory**
    * description - **Mandatory**
    * conf
    * optionsvip
        * option
    * environments
        * environment

Create List of Environment Vips
===============================

Here you need to call create() method at envvip_module.

You need to pass 1 parameter:
    * **environments**: List containing environment vips that you want to create.

Example:

.. code-block:: python

    envvips_to_create = [
        {
            "finalidade_txt": "FIN-TEST-1",
            "cliente_txt": "CLIENT-TEST-1",
            "ambiente_p44_txt": "AMBP44-TEST-1"
        },
        {
            "finalidade_txt": "FIN-TEST-2",
            "cliente_txt": "CLIENT-TEST-2",
            "ambiente_p44_txt": "AMBP44-TEST-2",
            "optionsvip": [
                {
                    "option": 1
                },
                {
                    "option": 2
                }
            ],
            "environments": [
                {
                    "environment": 1
                },
                {
                    "environment": 2
                }
            ]
        }
    ]

    envvip_module.create(environments=envvips_to_create)


PUT
***

Update List of Environment Vips
===============================

Here you need to call update() method at envvip_module.

You need to pass 1 parameter:
    * **environments**: List containing environment vips that you want to update.

Example:

.. code-block:: python

    envvips_to_update = [
        {
            "id": 1,
            "finalidade_txt": "FIN-TEST-1-NEW",
            "cliente_txt": "CLIENT-TEST-1-NEW",
            "ambiente_p44_txt": "AMBP44-TEST-1-NEW"
        },
        {
            "id": 2,
            "finalidade_txt": "FIN-TEST-2-NEW",
            "cliente_txt": "CLIENT-TEST-2-NEW",
            "ambiente_p44_txt": "AMBP44-TEST-2-NEW",
            "optionsvip": [
                {
                    "option": 3
                },
                {
                    "option": 4
                }
            ],
            "environments": [
                {
                    "environment": 3
                },
                {
                    "environment": 5
                }
            ]
        }
    ]

    envvip_module.update(environments=envvips_to_update)


DELETE
******

Delete List of Environment Vips
===============================

Here you need to call delete() method at envvip_module.

You need to pass 1 parameter:
    * **ids**: List containing identifiers of environment vips that you want to delete.

Example:

.. code-block:: python

    envvip_module.delete(ids=[1, 2, 3])

