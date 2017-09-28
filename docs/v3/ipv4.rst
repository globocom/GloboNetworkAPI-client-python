Using IPv4 module
#################

Assuming that you have Client Factory instantiated (see :ref:`How to Instantiate Client Factory <client-factory>`) at **client** variable, in order to access methods relative to IPv4 module you need to call create_api_ipv4() at **client**.

Example:

.. code-block:: python

   ipv4_module = client.create_api_ipv4()

For more information, please look GloboNetworkAPI documentation.

GET
***

The List of fields available at IPv4 module is:

    * id
    * ip_formated
    * oct1
    * oct2
    * oct3
    * oct4
    * networkipv4
    * description
    * equipments
    * vips
    * server_pool_members

Obtain List of IPv4's through id's
==================================

Here you need to call get() method at ipv4_module.

You can pass up to 5 parameters:
    * **ids**: List containing identifiers of IPv4's.
    * **include**: Array containing fields to include on response.
    * **exclude**: Array containing fields to exclude on response.
    * **fields**: Array containing fields to override default fields.
    * **kind**: string where you can choose between "basic" or "details".

The response will be a dict with a list of IPv4's.

Examples:

.. code-block:: python

    ipv4s = ipv4_module.get(ids=[1, 2, 3])

.. code-block:: python

    ipv4s = ipv4_module.get(ids=[1, 2, 3],
                           include=['oct1', 'oct2'],
                           exclude=['oct3'],
                           kind='details')

.. code-block:: python

    ipv4s = ipv4_module.get(ids=[1, 2, 3],
                           fields=['id', 'oct1', 'oct2', 'networkipv4'])

Obtain List of IPv4's through extended search
=============================================

Here you need to call search() method at ipv4_module.

You can pass up to 5 parameters:
    * **search**: Dict containing QuerySets to find IPv4's.
    * **include**: Array containing fields to include on response.
    * **exclude**: Array containing fields to exclude on response.
    * **fields**: Array containing fields to override default fields.
    * **kind**: string where you can choose between "basic" or "details".

The response will be a dict with a list of IPv4's.

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
    fields = ['id', 'oct1', 'oct2', 'vips']

    ipv4s = ipv4_module.search(search=search, fields=fields)

POST
****

The List of fields available for create an IPv4 is:

    * oct1
    * oct2
    * oct3
    * oct4
    * networkipv4 - **Mandatory**
    * description
    * equipments
        * id

Create List of IPv4's
=====================

Here you need to call create() method at ipv4_module.

You need to pass 1 parameter:
    * **ipv4s**: List containing IPv4's that you want to create.

Example:

.. code-block:: python

    ipv4s_to_create = [
        {
            "oct1": 10,
            "oct2": 10,
            "oct3": 0,
            "oct4": 2,
            "description": "IP 2",
            "networkipv4": 1
        },
        {
            "description": "IP 1",
            "networkipv4": 2,
            "equipments": [
                {
                    "id": 1
                },
                {
                    "id": 2
                }
            ]
        }
    ]

    ipv4_module.create(ipv4s=ipv4s_to_create)

PUT
***

The List of fields available for update an IPv4 is:

    * id - **Mandatory**
    * description
    * equipments
        * id

Update List of IPv4's
=====================

Here you need to call update() method at ipv4_module.

You need to pass 1 parameter:
    * **ipv4s**: List containing ipv4s that you want to update.

Example:

.. code-block:: python

    ipv4s_to_update = [
        {
            "id": 1,
            "description": "New-Desc-1"
        },
        {
            "id": 2,
            "equipments": [
                {
                    "id": 1
                },
                {
                    "id": 2
                }
            ]
        }
    ]

    ipv4_module.update(ipv4s=ipv4s_to_update)


DELETE
******

Delete List of IPv4's
=====================

Here you need to call delete() method at ipv4_module.

You need to pass 1 parameter:
    * **ids**: List containing identifiers of IPv4's that you want to delete.

Example:

.. code-block:: python

    ipv4_module.delete(ids=[1, 2, 3])

