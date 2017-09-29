Using IPv6 module
#################

Assuming that you have Client Factory instantiated (see :ref:`How to Instantiate Client Factory <client-factory>`) at **client** variable, in order to access methods relative to IPv6 module you need to call create_api_v4_ipv6() at **client**.

Example:

.. code-block:: python

   ipv6_module = client.create_api_v4_ipv6()

For more information, please look GloboNetworkAPI documentation.

GET
***

The List of fields available at IPv6 module is:

    * id
    * ip_formated
    * block1
    * block2
    * block3
    * block4
    * block5
    * block6
    * block7
    * block8
    * networkipv6
    * description
    * equipments
    * vips
    * server_pool_members

Obtain List of IPv6's through id's
==================================

Here you need to call get() method at ipv6_module.

You can pass up to 5 parameters:
    * **ids**: List containing identifiers of IPv6's.
    * **include**: Array containing fields to include on response.
    * **exclude**: Array containing fields to exclude on response.
    * **fields**: Array containing fields to override default fields.
    * **kind**: string where you can choose between "basic" or "details".

The response will be a dict with a list of IPv6's.

Examples:

.. code-block:: python

    ipv6s = ipv6_module.get(ids=[1, 2, 3])

.. code-block:: python

    ipv6s = ipv6_module.get(ids=[1, 2, 3],
                            include=['block1', 'block2'],
                            exclude=['block3'],
                            kind='details')

.. code-block:: python

    ipv6s = ipv6_module.get(ids=[1, 2, 3],
                            fields=['id', 'block1', 'block2', 'networkipv6'])

Obtain List of IPv6's through extended search
=============================================

Here you need to call search() method at ipv6_module.

You can pass up to 5 parameters:
    * **search**: Dict containing QuerySets to find IPv6's.
    * **include**: Array containing fields to include on response.
    * **exclude**: Array containing fields to exclude on response.
    * **fields**: Array containing fields to override default fields.
    * **kind**: string where you can choose between "basic" or "details".

The response will be a dict with a list of IPv6's.

Example:

.. code-block:: python

    search = {
        'extends_search': [{
            {
                "block1": "fefe"
            },
            {
                "block1": "fdfd"
            }
        }],
        'start_record': 0,
        'custom_search': '',
        'end_record': 25,
        'asorting_cols': [],
        'searchable_columns': []}
    fields = ['id', 'block1', 'block2', 'vips']

    ipv6s = ipv6_module.search(search=search, fields=fields)

POST
****

The List of fields available for create an IPv6 is:

    * block1
    * block2
    * block3
    * block4
    * block5
    * block6
    * block7
    * block8
    * networkipv6 - **Mandatory**
    * description
    * equipments
        * equipment
            * id
        * virtual_interface
            * id

Create List of IPv6's
=====================

Here you need to call create() method at ipv6_module.

You need to pass 1 parameter:
    * **ipv6s**: List containing IPv6's that you want to create.

Example:

.. code-block:: python

    ipv6s_to_create = [
        {

            "block1": "fefe"
            "block2": "a0a0"
            "block3": "a0a0"
            "block4": "a0a0"
            "block5": "0000"
            "block6": "0000"
            "block7": "0000"
            "block8": "0002"
            "description": "IP 2",
            "networkipv6": 1
        },
        {
            "description": "IP 1",
            "networkipv6": 2,
            "equipments": [
                {
                    "equipment": {
                        "id": 1
                    },
                    "virtual_interface": {
                        "id": 1
                    }
                },
                {
                    "equipment": {
                        "id": 2
                    },
                    "virtual_interface": {
                        "id": 2
                    }
                }
            ]
        }
    ]

    ipv6_module.create(ipv6s=ipv6s_to_create)

PUT
***

The List of fields available for update an IPv6 is:

    * id - **Mandatory**
    * description
    * equipments
        * equipment
            * id
        * virtual_interface
            * id

Update List of IPv6's
=====================

Here you need to call update() method at ipv6_module.

You need to pass 1 parameter:
    * **ipv6s**: List containing ipv6s that you want to update.

Example:

.. code-block:: python

    ipv6s_to_update = [
        {
            "id": 1,
            "description": "New-Desc-1"
        },
        {
            "id": 2,
            "equipments": [
                {
                    "equipment": {
                        "id": 2
                    },
                    "virtual_interface": {
                        "id": 2
                    }
                },
                {
                    "equipment": {
                        "id": 4
                    },
                    "virtual_interface": {
                        "id": 4
                    }
                }
            ]
        }
    ]

    ipv6_module.update(ipv6s=ipv6s_to_update)


DELETE
******

Delete List of IPv6's
=====================

Here you need to call delete() method at ipv6_module.

You need to pass 1 parameter:
    * **ids**: List containing identifiers of IPv6's that you want to delete.

Example:

.. code-block:: python

    ipv6_module.delete(ids=[1, 2, 3])

