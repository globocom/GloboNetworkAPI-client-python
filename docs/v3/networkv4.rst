Using NetworkIPv4 module
########################

Assuming that you have Client Factory instantiated (see :ref:`How to Instantiate Client Factory <client-factory>`) at **client** variable, in order to access methods relative to NetworkIPv4 module you need to call create_api_network_ipv4() at **client**.

Example:

.. code-block:: python

   netipv4_module = client.create_api_network_ipv4()

For more information, please look GloboNetworkAPI documentation.

GET
***

The List of fields available at NetworkIPv4 module is:

    * id
    * oct1
    * oct2
    * oct3
    * oct4
    * prefix
    * networkv4
    * mask_oct1
    * mask_oct2
    * mask_oct3
    * mask_oct4
    * mask_formated
    * broadcast
    * vlan
    * network_type
    * environmentvip
    * active
    * dhcprelay
    * cluster_unit

Obtain List of NetworkIPv4's through id's
=========================================

Here you need to call get() method at netipv4_module.

You can pass up to 5 parameters:
    * **ids**: List containing identifiers of NetworkIPv4's.
    * **include**: Array containing fields to include on response.
    * **exclude**: Array containing fields to exclude on response.
    * **fields**: Array containing fields to override default fields.
    * **kind**: string where you can choose between "basic" or "details".

The response will be a dict with a list of NetworkIPv4's.

Examples:

.. code-block:: python

    netipv4s = netipv4_module.get(ids=[1, 2, 3])

.. code-block:: python

    netipv4s = netipv4_module.get(ids=[1, 2, 3],
                                  include=['oct1', 'oct2'],
                                  exclude=['oct3'],
                                  kind='details')

.. code-block:: python

    netipv4s = netipv4_module.get(ids=[1, 2, 3],
                                  fields=['id', 'oct1', 'oct2', 'networkv4'])

Obtain List of NetworkIPv4's through extended search
====================================================

Here you need to call search() method at netipv4_module.

You can pass up to 5 parameters:
    * **search**: Dict containing QuerySets to find NetworkIPv4's.
    * **include**: Array containing fields to include on response.
    * **exclude**: Array containing fields to exclude on response.
    * **fields**: Array containing fields to override default fields.
    * **kind**: string where you can choose between "basic" or "details".

The response will be a dict with a list of NetworkIPv4's.

Example:

.. code-block:: python

    search = {
        'extends_search': [{
            {
                'oct1': 10,
            },
            {
                'oct1': 172,
            }
        }],
        'start_record': 0,
        'custom_search': '',
        'end_record': 25,
        'asorting_cols': [],
        'searchable_columns': []}
    fields = ['id', 'oct1', 'oct2', 'vlan']

    netipv4s = netipv4_module.search(search=search, fields=fields)

POST
****

The List of fields available for create an NetworkIPv4 is:

    * oct1
    * oct2
    * oct3
    * oct4
    * prefix
    * mask_oct1
    * mask_oct2
    * mask_oct3
    * mask_oct4
    * vlan - **Mandatory**
    * network_type
    * environmentvip
    * cluster_unit
    * active

Create List of NetworkIPv4's
============================

Here you need to call create() method at netipv4_module.

You need to pass 1 parameter:
    * **networkipv4s**: List containing NetworkIPv4's that you want to create.

Example:

.. code-block:: python

    netipv4s_to_create = [
        {
            "vlan": 1
        },
        {
            "oct1": 10,
            "oct2": 10,
            "oct3": 10,
            "oct4": 0,
            "prefix": 24,
            "mask_oct1": 255,
            "mask_oct2": 255,
            "mask_oct3": 255,
            "mask_oct4": 0,
            "vlan": 2,
            "network_type": 3,
            "environmentvip": 2,
            "cluster_unit": "anything"
        }
    ]

    netipv4_module.create(networkipv4s=netipv4s_to_create)

PUT
***

The List of fields available for update an NetworkIPv4 is:

    * id - **Mandatory**
    * network_type - **Mandatory**
    * environmentvip
    * cluster_unit
    * active

Update List of NetworkIPv4's
============================

Here you need to call update() method at netipv4_module.

You need to pass 1 parameter:
    * **networkipv4s**: List containing ipv4s that you want to update.

Example:

.. code-block:: python

    netipv4s_to_update = [
        {
            "id": 1,
            "networktype": 5
        },
        {
            "id": 2,
            "active": True,
            "network_type": 4,
            "environmentvip": 5,
            "cluster_unit": "anything"
        }
    ]

    netipv4_module.update(networkipv4s=netipv4s_to_update)

DELETE
******

Delete List of NetworkIPv4's
============================

Here you need to call delete() method at netipv4_module.

You need to pass 1 parameter:
    * **ids**: List containing identifiers of NetworkIPv4's that you want to delete.

Example:

.. code-block:: python

    netipv4_module.delete(ids=[1, 2, 3])

