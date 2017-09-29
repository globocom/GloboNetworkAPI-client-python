Using Neighbor module
########################

Assuming that you have Client Factory instantiated (see :ref:`How to Instantiate Client Factory <client-factory>`) at **client** variable, in order to access methods relative to Neighbor module you need to call create_api_v4_neighbor() at **client**.

Example:

.. code-block:: python

   neighbor_module = client.create_api_v4_neighbor()

For more information, please look GloboNetworkAPI documentation.

GET
***

The List of fields available at Neighbor module is:

    * id
    * remote_as
    * remote_ip
    * password
    * maximum_hops
    * timer_keepalive
    * timer_timeout
    * description
    * soft_reconfiguration
    * community
    * remove_private_as
    * next_hop_self
    * kind
    * created
    * virtual_interface

Obtain List of Neighbors through id's
========================================

Here you need to call get() method at neighbor_module.

You can pass up to 5 parameters:
    * **ids**: List containing identifiers of neighbors.
    * **include**: Array containing fields to include on response.
    * **exclude**: Array containing fields to exclude on response.
    * **fields**: Array containing fields to override default fields.
    * **kind**: string where you can choose between "basic" or "details".

The response will be a dict with a list of Neighbors.

Examples:

.. code-block:: python

    neighbors = neighbor_module.get(ids=[1, 2, 3])

.. code-block:: python

    neighbors = neighbor_module.get(ids=[1, 2, 3],
                                    include=['virtual_interface', 'kind'],
                                    exclude=['id'])
.. code-block:: python

    neighbors = neighbor_module.get(ids=[1, 2, 3],
                                    fields=['id', 'remote_as', 'remote_ip'])

Obtain List of Neighbors through extended search
===================================================

Here you need to call search() method at neighbor_module.

You can pass up to 5 parameters:
    * **search**: Dict containing QuerySets to find neighbors.
    * **include**: Array containing fields to include on response.
    * **exclude**: Array containing fields to exclude on response.
    * **fields**: Array containing fields to override default fields.
    * **kind**: string where you can choose between "basic" or "details".

The response will be a dict with a list of Neighbors.

Example:

.. code-block:: python

    search = {
        'extends_search': [{
            "community": false
        }],
        'start_record': 0,
        'custom_search': '',
        'end_record': 25,
        'asorting_cols': [],
        'searchable_columns': []}
    fields = ['id', 'remote_as']

    neighbors = neighbor_module.search(search=search, fields=fields)

POST
****

The List of fields available for create an Neighbor is:

    * remote_as
    * remote_ip
    * password
    * maximum_hops
    * timer_keepalive
    * timer_timeout
    * description
    * soft_reconfiguration
    * community
    * remove_private_as
    * next_hop_self
    * kind
    * virtual_interface - **Mandatory**

Create List of Neighbors
===========================

Here you need to call create() method at neighbor_module.

You need to pass 1 parameter:
    * **neighbors**: List containing neighbors that you want to create.

Example:

.. code-block:: python

    neighbors_to_create = [
        {
            "remote_as": "203",
            "remote_ip": "10.10.0.2",
            "password": "Test-pwd",
            "maximum_hops": "5",
            "timer_keepalive": "3",
            "timer_timeout": "60",
            "description": "any",
            "soft_reconfiguration": False,
            "community": True,
            "remove_private_as": True,
            "next_hop_self": False,
            "kind": "I",
            "virtual_interface": 1,
        },
        {
            "remote_as": "203",
            "remote_ip": "10.10.0.3",
            "password": "Test-pwd",
            "maximum_hops": "5",
            "timer_keepalive": "3",
            "timer_timeout": "60",
            "description": "any",
            "soft_reconfiguration": False,
            "community": True,
            "remove_private_as": True,
            "next_hop_self": True,
            "kind": "E",
            "virtual_interface": 2
        }
    ]

    neighbor_module.create(neighbors=neighbors_to_create)


PUT
***

The List of fields available for update an Neighbor is:

    * id - **Mandatory**
    * remote_as
    * remote_ip
    * password
    * maximum_hops
    * timer_keepalive
    * timer_timeout
    * description
    * soft_reconfiguration
    * community
    * remove_private_as
    * next_hop_self
    * kind
    * virtual_interface - **Mandatory**

Update List of Neighbors
===========================

Here you need to call update() method at neighbor_module.

You need to pass 1 parameter:
    * **neighbors**: List containing neighbors that you want to update.

Example:

.. code-block:: python

    neighbors_to_update = [
        {
            "id": 1,
            "remote_as": "203",
            "remote_ip": "10.10.0.4",
            "password": "Test-pwd",
            "maximum_hops": "5",
            "timer_keepalive": "4",
            "timer_timeout": "70",
            "description": "any",
            "soft_reconfiguration": False,
            "community": True,
            "remove_private_as": True,
            "next_hop_self": False,
            "kind": "I",
            "virtual_interface": 3,
        },
        {
            "id": 2,
            "remote_as": "203",
            "remote_ip": "10.10.0.5",
            "password": "Test-pwd-2",
            "maximum_hops": "7",
            "timer_keepalive": "3",
            "timer_timeout": "70",
            "description": "any",
            "soft_reconfiguration": True,
            "community": True,
            "remove_private_as": True,
            "next_hop_self": True,
            "kind": "E",
            "virtual_interface": 2
        }
    ]

    neighbor_module.update(neighbors=neighbors_to_update)


DELETE
******

Delete List of Neighbors
===========================

Here you need to call delete() method at neighbor_module.

You need to pass 1 parameter:
    * **ids**: List containing identifiers of neighbors that you want to delete.

Example:

.. code-block:: python

    neighbor_module.delete(ids=[1, 2, 3])

