Using Object Group Permission module
####################################

Assuming that you have Client Factory instantiated (see :ref:`How to Instantiate Client Factory <client-factory>`) at **client** variable, in order to access methods relative to Object Group Permission module you need to call create_api_object_group_permission() at **client**.

Example:

.. code-block:: python

   ogp_module = client.create_api_object_group_permission()

For more information, please look GloboNetworkAPI documentation.

GET
***

The List of fields available at Object Group Permission module is:

    * id
    * user_group
    * object_type
    * object_value
    * read
    * write
    * change_config
    * delete

Obtain List of Object Group Permissions through id's
====================================================

Here you need to call get() method at ogp_module.

You can pass up to 5 parameters:
    * **ids**: List containing identifiers of Object Group Permissions.
    * **include**: Array containing fields to include on response.
    * **exclude**: Array containing fields to exclude on response.
    * **fields**: Array containing fields to override default fields.
    * **kind**: string where you can choose between "basic" or "details".

The response will be a dict with a list of Object Group Permissions.

Examples:

.. code-block:: python

    ogps = ogp_module.get(ids=[1, 2, 3])

.. code-block:: python

    ogps = ogp_module.get(ids=[1, 2, 3],
                          include=['read'],
                          exclude=['write', 'delete'],
                          kind='basic')

.. code-block:: python

    ogps = ogp_module.get(ids=[1, 2, 3],
                          fields=['id', 'read', 'delete'])

Obtain List of Object Group Permissions through extended search
===============================================================

Here you need to call search() method at ogp_module.

You can pass up to 5 parameters:
    * **search**: Dict containing QuerySets to find Object Group Permissions.
    * **include**: Array containing fields to include on response.
    * **exclude**: Array containing fields to exclude on response.
    * **fields**: Array containing fields to override default fields.
    * **kind**: string where you can choose between "basic" or "details".

The response will be a dict with a list of Object Group Permissions.

Example:

.. code-block:: python

    search = {
        'extends_search': [{
            "read": True
        }],
        'start_record': 0,
        'custom_search': '',
        'end_record': 25,
        'asorting_cols': [],
        'searchable_columns': []}
    fields = ['id', 'user_group', 'read']

    ogps = ogp_module.search(search=search, fields=fields)

POST
****

The List of fields available for create an Object Group Permission is:

    * user_group - **Mandatory**
    * object_type - **Mandatory**
    * object_value - **Mandatory**
    * read - **Mandatory**
    * write - **Mandatory**
    * change_config - **Mandatory**
    * delete - **Mandatory**

Create List of Object Group Permissions
=======================================

Here you need to call create() method at ogp_module.

You need to pass 1 parameter:
    * **ogps**: List containing Object Group Permissions that you want to create.

Example:

.. code-block:: python

    ogps_to_create = [
        {
            "user_group": 1,
            "object_type": 2,
            "object_value": 1,
            "read": True,
            "write": True,
            "change_config": True,
            "delete": False
        },
        {
            "user_group": 1,
            "object_type": 2,
            "object_value": 4,
            "read": True,
            "write": True,
            "change_config": True,
            "delete": False
        }
    ]

    ogp_module.create(ogps=ogps_to_create)

PUT
***

The List of fields available for update an Object Group Permission is:

    * id - **Mandatory**
    * read
    * write
    * change_config
    * delete

Update List of Object Group Permissions
=======================================

Here you need to call update() method at ogp_module.

You need to pass 1 parameter:
    * **ogps**: List containing Object Group Permissions that you want to update.

Example:

.. code-block:: python

    ogps_to_update = [
        {
            "id": 1,
            "read": False,
            "write": False,
            "change_config": True,
            "delete": False
        },
        {
            "id": 2,
            "read": False,
            "write": False,
            "change_config": True,
            "delete": False
        }
    ]

    ogp_module.update(ogps=ogps_to_update)


DELETE
******

Delete List of Object Group Permissions
=======================================

Here you need to call delete() method at ogp_module.

You need to pass 1 parameter:
    * **ids**: List containing identifiers of Object Group Permissions that you want to delete.

Example:

.. code-block:: python

    ogp_module.delete(ids=[1, 2, 3])

