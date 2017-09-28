Using Vrf module
########################

Assuming that you have Client Factory instantiated (see :ref:`How to Instantiate Client Factory <client-factory>`) at **client** variable, in order to access methods relative to Vrf module you need to call create_api_vrf() at **client**.

Example:

.. code-block:: python

   vrf_module = client.create_api_vrf()

For more information, please look GloboNetworkAPI documentation.

GET
***

The List of fields available at Vrf module is:

    * id
    * internal_name
    * vrf

Obtain List of Vrfs through id's
========================================

Here you need to call get() method at vrf_module.

You can pass up to 5 parameters:
    * **ids**: List containing identifiers of vrfs.
    * **include**: Array containing fields to include on response.
    * **exclude**: Array containing fields to exclude on response.
    * **fields**: Array containing fields to override default fields.
    * **kind**: string where you can choose between "basic" or "details".

The response will be a dict with a list of Vrfs.

Examples:

.. code-block:: python

    vrfs = vrf_module.get(ids=[1, 2, 3])

Obtain List of Vrfs through extended search
===================================================

Here you need to call search() method at vrf_module.

You can pass up to 5 parameters:
    * **search**: Dict containing QuerySets to find vrfs.
    * **include**: Array containing fields to include on response.
    * **exclude**: Array containing fields to exclude on response.
    * **fields**: Array containing fields to override default fields.
    * **kind**: string where you can choose between "basic" or "details".

The response will be a dict with a list of Vrfs.

Example:

.. code-block:: python

    search = {
        'extends_search': [{
            "vrf__contains": "Default"
        }],
        'start_record': 0,
        'custom_search': '',
        'end_record': 25,
        'asorting_cols': [],
        'searchable_columns': []}
    fields = ['id', 'name']

    vrfs = vrf_module.search(search=search, fields=fields)

POST
****

The List of fields available for create an Vrf is:

    * vrf - **Mandatory**
    * internal_name - **Mandatory**

Create List of Vrfs
===========================

Here you need to call create() method at vrf_module.

You need to pass 1 parameter:
    * **vrfs**: List containing vrfs that you want to create.

Example:

.. code-block:: python

    vrfs_to_create = [
        {
            "vrf": "VrfTest-1",
            "internal_name": "VrfTest-1"
        },
        {
            "vrf": "VrfTest-2",
            "internal_name": "VrfTest-2"
        }
    ]

    vrf_module.create(vrfs=vrfs_to_create)


PUT
***

The List of fields available for update an Vrf is:

    * id - **Mandatory**
    * vrf - **Mandatory**
    * internal_name - **Mandatory**

Update List of Vrfs
===========================

Here you need to call update() method at vrf_module.

You need to pass 1 parameter:
    * **vrfs**: List containing vrfs that you want to update.

Example:

.. code-block:: python

    vrfs_to_update = [
        {
            "id": 1,
            "vrf": "VrfTest-1",
            "internal_name": "VrfTest-1"
        },
        {
            "id": 2,
            "vrf": "VrfTest-2",
            "internal_name": "VrfTest-2"
        }
    ]

    vrf_module.update(vrfs=vrfs_to_update)


DELETE
******

Delete List of Vrfs
===========================

Here you need to call delete() method at vrf_module.

You need to pass 1 parameter:
    * **ids**: List containing identifiers of vrfs that you want to delete.

Example:

.. code-block:: python

    vrf_module.delete(ids=[1, 2, 3])

