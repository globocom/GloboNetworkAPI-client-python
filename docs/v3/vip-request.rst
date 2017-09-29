Using Vip Request module
########################

Assuming that you have Client Factory instantiated (see :ref:`How to Instantiate Client Factory <client-factory>`) at **client** variable, in order to access methods relative to Vip Request module you need to call create_api_vip_request() at **client**.

Example:

.. code-block:: python

   vip_module = client.create_api_vip_request()

For more information, please look GloboNetworkAPI documentation.

GET
***

The List of fields available at Vip Request module is:

    * id
    * name
    * service
    * business
    * environmentvip
    * ipv4
    * ipv6
    * equipments
    * default_names
    * dscp
    * ports
    * options
    * groups_permissions
    * created

Obtain List of Vip Requests through id's
========================================

Here you need to call get() method at vip_module.

You can pass up to 5 parameters:
    * **ids**: List containing identifiers of vip requests.
    * **include**: Array containing fields to include on response.
    * **exclude**: Array containing fields to exclude on response.
    * **fields**: Array containing fields to override default fields.
    * **kind**: string where you can choose between "basic" or "details".

The response will be a dict with a list of Vip Requests.

Examples:

.. code-block:: python

    vips = vip_module.get(ids=[1, 2, 3])

.. code-block:: python

    vips = vip_module.get(ids=[1, 2, 3],
                          include=['name', 'service'],
                          exclude=['id'],
                          kind='details')

.. code-block:: python

    vips = vip_module.get(ids=[1, 2, 3],
                          fields=['id', 'name', 'ipv4'])

Obtain List of Vip Requests through extended search
===================================================

Here you need to call search() method at vip_module.

You can pass up to 5 parameters:
    * **search**: Dict containing QuerySets to find vip requests.
    * **include**: Array containing fields to include on response.
    * **exclude**: Array containing fields to exclude on response.
    * **fields**: Array containing fields to override default fields.
    * **kind**: string where you can choose between "basic" or "details".

The response will be a dict with a list of Vip Requests.

Example:

.. code-block:: python

    search = {
        'extends_search': [
            {
                "ipv4__oct1": "192",
                "ipv4__oct2": "168",
                "created": true
            },
            {
                "ipv4__oct2": "168",
                "ipv4__oct3": "17",
                "created": false
            }
        ],
        'start_record': 0,
        'custom_search': '',
        'end_record': 25,
        'asorting_cols': [],
        'searchable_columns': []
    }
    fields = ['id', 'name']

    vips = vip_module.search(search=search, fields=fields)

POST
****

The List of fields available for create an Vip Request is:

    * business
    * created
    * environmentvip
    * id
    * ipv4
    * ipv6
    * name
    * options
        * cache_group
        * persistence
        * timeout
        * traffic_return
    * ports
        * id
        * options
            * l4_protocol
            * l7_protocol
        * pools
            * l7_rule - **Mandatory**
            * l7_value
            * order
            * server_pool - **Mandatory**
        * port
    * service
    * groups_permissions
        * user_group - **Mandatory**
        * read - **Mandatory**
        * write - **Mandatory**
        * delete - **Mandatory**
        * change_config - **Mandatory**
    * users_permissions
        * user - **Mandatory**
        * read - **Mandatory**
        * write - **Mandatory**
        * delete - **Mandatory**
        * change_config - **Mandatory**

Create List of Vip Requests
===========================

Here you need to call create() method at vip_module.

You need to pass 1 parameter:
    * **vips**: List containing vip requests that you want to create.

Example:

.. code-block:: python

    vips_to_create = [
        {
            "business": "some-business",
            "environmentvip": 2,
            "ipv4": 1,
            "ipv6": 44,
            "name": "vip.test.com",
            "options": {
                "cache_group": 2,
                "persistence": 3,
                "timeout": 41,
                "traffic_return": 20
            },
            "ports": [
                {
                    "options": {
                        "l4_protocol": 32,
                        "l7_protocol": 31
                    },
                    "pools": [
                        {
                            "l7_rule": 34,
                            "order": 1,
                            "server_pool": 3
                        }
                    ],
                    "port": 8181
                },
                {
                    "options": {
                        "l4_protocol": 33,
                        "l7_protocol": 34
                    },
                    "pools": [
                        {
                            "l7_rule": 37,
                            "order": 0,
                            "server_pool": 4
                        }
                    ],
                    "port": 9090
                }
            ],
            "service": "some-service"
        }
    ]

    vip_module.create(vips=vips_to_create)


PUT
***

The List of fields available for update an Vip Request is:

    * id - **Mandatory**
    * business
    * created
    * environmentvip
    * id
    * ipv4
    * ipv6
    * name
    * options
        * cache_group
        * persistence
        * timeout
        * traffic_return
    * ports
        * id
        * options
            * l4_protocol
            * l7_protocol
        * pools
            * l7_rule - **Mandatory**
            * l7_value
            * order
            * server_pool - **Mandatory**
        * port
    * service
    * groups_permissions
        * user_group - **Mandatory**
        * read - **Mandatory**
        * write - **Mandatory**
        * delete - **Mandatory**
        * change_config - **Mandatory**
    * users_permissions
        * user - **Mandatory**
        * read - **Mandatory**
        * write - **Mandatory**
        * delete - **Mandatory**
        * change_config - **Mandatory**

Update List of Vip Requests
===========================

Here you need to call update() method at vip_module.

You need to pass 1 parameter:
    * **vips**: List containing vip requests that you want to update.

Example:

.. code-block:: python

    vips_to_update = [
        {
            "id": 1,
            "business": "some-business-2",
            "environmentvip": 3,
            "ipv4": 2,
            "ipv6": 43,
            "name": "vipnew.test.com",
            "options": {
                "cache_group": 1,
                "persistence": 3,
                "timeout": 40,
                "traffic_return": 9
            },
            "ports": [
                {
                    "options": {
                        "l4_protocol": 2,
                        "l7_protocol": 1
                    },
                    "pools": [
                        {
                            "l7_rule": 24,
                            "order": 1,
                            "server_pool": 3
                        }
                    ],
                    "port": 8181
                },
                {
                    "options": {
                        "l4_protocol": 3,
                        "l7_protocol": 4
                    },
                    "pools": [
                        {
                            "l7_rule": 27,
                            "order": 0,
                            "server_pool": 4
                        }
                    ],
                    "port": 9191
                }
            ],
            "service": "some-new-service"
        }
    ]

    vip_module.update(vips=vips_to_update)


DELETE
******

Delete List of Vip Requests
===========================

Here you need to call delete() method at vip_module.

You need to pass 1 parameter:
    * **ids**: List containing identifiers of vip requests that you want to delete.

Example:

.. code-block:: python

    vip_module.delete(ids=[1, 2, 3])

