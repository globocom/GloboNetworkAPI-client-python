Using NetworkIPv6 module
########################

Assuming that you have Client Factory instantiated (see :ref:`How to Instantiate Client Factory <client-factory>`) at **client** variable, in order to access methods relative to NetworkIPv6 module you need to call create_api_network_ipv6() at **client**.

Example:

.. code-block:: python

   netipv6_module = client.create_api_network_ipv6()

For more information, please look GloboNetworkAPI documentation.

GET
***

The List of fields available at NetworkIPv6 module is:

    * id
    * block1
    * block2
    * block3
    * block4
    * block5
    * block6
    * block7
    * block8
    * prefix
    * networkv6
    * mask1
    * mask2
    * mask3
    * mask4
    * mask5
    * mask6
    * mask7
    * mask8
    * mask_formated

Obtain List of NetworkIPv6's through id's
=========================================

Here you need to call get() method at netipv6_module.

You can pass up to 5 parameters:
    * **ids**: List containing identifiers of NetworkIPv6's.
    * **include**: Array containing fields to include on response.
    * **exclude**: Array containing fields to exclude on response.
    * **fields**: Array containing fields to override default fields.
    * **kind**: string where you can choose between "basic" or "details".

The response will be a dict with a list of NetworkIPv6's.

Examples:

.. code-block:: python

    netipv6s = netipv6_module.get(ids=[1, 2, 3])

.. code-block:: python

    netipv6s = netipv6_module.get(ids=[1, 2, 3],
                                  include=['block1', 'block2'],
                                  exclude=['block3'],
                                  kind='details')

.. code-block:: python

    netipv6s = netipv6_module.get(ids=[1, 2, 3],
                                  fields=['id', 'block1', 'block2', 'networkv6'])

Obtain List of NetworkIPv6's through extended search
====================================================

Here you need to call search() method at netipv6_module.

You can pass up to 5 parameters:
    * **search**: Dict containing QuerySets to find NetworkIPv6's.
    * **include**: Array containing fields to include on response.
    * **exclude**: Array containing fields to exclude on response.
    * **fields**: Array containing fields to override default fields.
    * **kind**: string where you can choose between "basic" or "details".

The response will be a dict with a list of NetworkIPv6's.

Example:

.. code-block:: python

    search = {
        'extends_search': [{
            {
                "block1": "fefe"
            },
            {
                "block1": "fdbe"
            }
        }],
        'start_record': 0,
        'custom_search': '',
        'end_record': 25,
        'asorting_cols': [],
        'searchable_columns': []}
    fields = ['id', 'block1', 'block2', 'mask_formated']

    netipv6s = netipv6_module.search(search=search, fields=fields)

POST
****

The List of fields available for create an NetworkIPv6 is:

    * block1
    * block2
    * block3
    * block4
    * block5
    * block6
    * block7
    * block8
    * prefix
    * mask
    * mask
    * mask
    * mask
    * mask
    * mask
    * mask
    * mask
    * vlan - **Mandatory**
    * network_type
    * environmentvip
    * cluster_unit
    * active

Create List of NetworkIPv6's
============================

Here you need to call create() method at netipv6_module.

You need to pass 1 parameter:
    * **networkipv6s**: List containing NetworkIPv6's that you want to create.

Example:

.. code-block:: python

    netipv6s_to_create = [
        {
            "vlan": 1
        },
        {
            "block1": "fdbe",
            "block2": "fdbe",
            "block3": "a0a0",
            "block4": "a0a0",
            "block5": "0000",
            "block6": "0000",
            "block7": "0000",
            "block8": "0000",
            "prefix": 64,
            "mask1": "ffff",
            "mask2": "ffff",
            "mask3": "ffff",
            "mask4": "ffff",
            "mask5": "0000",
            "mask6": "0000",
            "mask7": "0000",
            "mask8": "0000",
            "vlan": 2,
            "network_type": 3,
            "environmentvip": 2,
            "active": False,
            "cluster_unit": "anything"
        }
    ]

    netipv6_module.create(networkipv6s=netipv6s_to_create)

PUT
***

The List of fields available for update an NetworkIPv6 is:

    * id - **Mandatory**
    * network_type - **Mandatory**
    * environmentvip
    * cluster_unit
    * active

Update List of NetworkIPv6's
============================

Here you need to call update() method at netipv6_module.

You need to pass 1 parameter:
    * **networkipv6s**: List containing ipv6s that you want to update.

Example:

.. code-block:: python

    netipv6s_to_update = [
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

    netipv6_module.update(networkipv6s=netipv6s_to_update)

DELETE
******

Delete List of NetworkIPv6's
============================

Here you need to call delete() method at netipv6_module.

You need to pass 1 parameter:
    * **ids**: List containing identifiers of NetworkIPv6's that you want to delete.

Example:

.. code-block:: python

    netipv6_module.delete(ids=[1, 2, 3])

