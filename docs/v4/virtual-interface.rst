Using Virtual Interface module
##############################

Assuming that you have Client Factory instantiated (see :ref:`How to Instantiate Client Factory <client-factory>`) at **client** variable, in order to access methods relative to Virtual Interface module you need to call create_api_v4_virtual_interface() at **client**.

Example:

.. code-block:: python

   vi_module = client.create_api_v4_virtual_interface()

For more information, please look GloboNetworkAPI documentation.

GET
***

The List of fields available at Virtual Interface module is:

    * id
    * name
    * vrf

Obtain List of Virtual Interfaces through id's
==============================================

Here you need to call get() method at vi_module.

You can pass up to 5 parameters:
    * **ids**: List containing identifiers of virtual interfaces.
    * **include**: Array containing fields to include on response.
    * **exclude**: Array containing fields to exclude on response.
    * **fields**: Array containing fields to override default fields.
    * **kind**: string where you can choose between "basic" or "details".

The response will be a dict with a list of Virtual Interfaces.

Examples:

.. code-block:: python

    vis = vi_module.get(ids=[1, 2, 3])

.. code-block:: python

    vis = vi_module.get(ids=[1, 2, 3],
                        kind='basic')

.. code-block:: python

    vis = vi_module.get(ids=[1, 2, 3],
                        fields=['name'])

Obtain List of Virtual Interfaces through extended search
=========================================================

Here you need to call search() method at vi_module.

You can pass up to 5 parameters:
    * **search**: Dict containing QuerySets to find virtual interfaces.
    * **include**: Array containing fields to include on response.
    * **exclude**: Array containing fields to exclude on response.
    * **fields**: Array containing fields to override default fields.
    * **kind**: string where you can choose between "basic" or "details".

The response will be a dict with a list of Virtual Interfaces.

Example:

.. code-block:: python

    search = {
        'extends_search': [{
            "vrf__id": 1,
            "name__contains": "abc"
        }],
        'start_record': 0,
        'custom_search': '',
        'end_record': 25,
        'asorting_cols': [],
        'searchable_columns': []}
    fields = ['id', 'name']

    vis = vi_module.search(search=search, fields=fields)

POST
****

The List of fields available for create an Virtual Interface is:

    * vrf - **Mandatory**
    * name - **Mandatory**

Create List of Virtual Interfaces
=================================

Here you need to call create() method at vi_module.

You need to pass 1 parameter:
    * **virtual_interfaces**: List containing virtual interfaces that you want to create.

Example:

.. code-block:: python

    vis_to_create = [
        {
            "vrf": 1,
            "name": "Virt-1"
        },
        {
            "vrf": 2,
            "name": "Virt-2"
        }
    ]

    vi_module.create(virtual_interfaces=vis_to_create)


PUT
***

The List of fields available for update an Virtual Interface is:

    * id - **Mandatory**
    * vrf - **Mandatory**
    * name - **Mandatory**

Update List of Virtual Interfaces
=================================

Here you need to call update() method at vi_module.

You need to pass 1 parameter:
    * **virtual_interfaces**: List containing virtual interfaces that you want to update.

Example:

.. code-block:: python

    vis_to_update = [
        {
            "id": 1,
            "vrf": 1,
            "name": "Virt-3"
        },
        {
            "id": 2,
            "vrf": 4,
            "name": "Virt-2"
        }
    ]

    vi_module.update(virtual_interfaces=vis_to_update)

DELETE
******

Delete List of Virtual Interfaces
=================================

Here you need to call delete() method at vi_module.

You need to pass 1 parameter:
    * **ids**: List containing identifiers of virtual interfaces that you want to delete.

Example:

.. code-block:: python

    vi_module.delete(ids=[1, 2, 3])

