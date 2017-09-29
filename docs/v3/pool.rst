Using Server Pool module
########################

Assuming that you have Client Factory instantiated (see :ref:`How to Instantiate Client Factory <client-factory>`) at **client** variable, in order to access methods relative to Server Pool module you need to call create_api_pool() at **client**.


Example:

.. code-block:: python

   pool_module = client.create_api_pool()

For more information, please look GloboNetworkAPI documentation.

GET
***

The List of fields available at Server Pool module is:

    * id
    * identifier
    * default_port
    * environment
    * servicedownaction
    * lb_method
    * healthcheck
    * default_limit
    * server_pool_members
    * pool_created
    * vips
    * dscp
    * groups_permissions

Obtain List of Server Pools through id's
========================================

Here you need to call get() method at pool_module.

You can pass up to 5 parameters:
    * **ids**: List containing identifiers of server pools.
    * **include**: Array containing fields to include on response.
    * **exclude**: Array containing fields to exclude on response.
    * **fields**: Array containing fields to override default fields.
    * **kind**: string where you can choose between "basic" or "details".

The response will be a dict with a list of Server Pools.

Examples:

.. code-block:: python

    pools = pool_module.get(ids=[1, 2, 3])

.. code-block:: python

    pools = pool_module.get(ids=[1, 2, 3],
                            include=['identifier', 'healthcheck'],
                            exclude=['environment'],
                            kind='details')

.. code-block:: python

    pools = pool_module.get(ids=[1, 2, 3],
                            fields=['id', 'identifier', 'default_port'])

Obtain List of Server Pools through extended search
===================================================

Here you need to call search() method at pool_module.

You can pass up to 5 parameters:
    * **search**: Dict containing QuerySets to find server pools.
    * **include**: Array containing fields to include on response.
    * **exclude**: Array containing fields to exclude on response.
    * **fields**: Array containing fields to override default fields.
    * **kind**: string where you can choose between "basic" or "details".

The response will be a dict with a list of Server Pools.

Example:

.. code-block:: python

    search = {
        'extends_search': [{
            "environment": 1
        }],
        'start_record': 0,
        'custom_search': '',
        'end_record': 25,
        'asorting_cols': [],
        'searchable_columns': []}
    fields = ['id', 'identifier']

    pools = pool_module.search(search=search, fields=fields)

POST
****

The List of fields available for create a Server Pool is:

    * identifier - **Mandatory**
    * default_port - **Mandatory**
    * environment - **Mandatory**
    * servicedownaction - **Mandatory**
        * id
        * name - **Mandatory**
    * lb_method - **Mandatory**
    * healthcheck - **Mandatory**
        * identifier - **Mandatory**
        * healthcheck_type - **Mandatory**
        * healthcheck_request - **Mandatory**
        * healthcheck_expect - **Mandatory**
        * destination - **Mandatory**
    * default_limit - **Mandatory**
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
    * server_pool_members - **Mandatory**
        * ipv6 - **Mandatory**
            * id  - **Mandatory**
            * ip_formated - **Mandatory**
        * ip - **Mandatory**
            * id - **Mandatory**
            * ip_formated - **Mandatory**
        * priority - **Mandatory**
        * weight - **Mandatory**
        * limit - **Mandatory**
        * port_real - **Mandatory**
        * member_status - **Mandatory**

Create List of Server Pools
===========================

Here you need to call create() method at pool_module.

You need to pass 1 parameter:
    * **pools**: List containing server pools that you want to create.

Example:

.. code-block:: python

    pools_to_create = [
        {
            "lb_method": "least-conn",
            "server_pool_members": [

            ],
            "healthcheck": {
                "healthcheck_type": "TCP",
                "destination": "*:*",
                "healthcheck_expect": "",
                "identifier": "Test_1234",
                "healthcheck_request": ""
            },
            "environment": 4449,
            "servicedownaction": {
                "id": 1,
                "name": "something"
            },
            "default_port": 9943,
            "default_limit": 0,
            "identifier": "PoolTest"
        },
        {
            "lb_method": "least-conn",
            "server_pool_members":[
                {
                    "port_real": 5564,
                    "weight": 0,
                    "ip": {
                        "ip_formated": "10.134.9.201",
                        "id": 4
                    },
                    "priority": 0,
                    "limit": 0,
                    "member_status": 7,
                    "ipv6": {
                        "ip_formated": "fdbe:fdbe:0000:0000:0000:0000:0000:0002",
                        "id": 3
                    }
                },
                {
                    "port_real": 3456,
                    "weight": 0,
                    "ip": {
                        "ip_formated": "10.134.9.202",
                        "id": 5
                    },
                    "priority": 0,
                    "limit": 0,
                    "member_status": 7,
                    "ipv6": {
                        "ip_formated": "fdbe:fdbe:0000:0000:0000:0000:0000:0002",
                        "id": 3
                    }
                }
            ],
            "healthcheck":{
                "healthcheck_type": "HTTP",
                "destination": "*:14500",
                "healthcheck_expect": "",
                "identifier": "Test_8787",
                "healthcheck_request": ""
            },
            "environment": 543,
            "servicedownaction":{
                "id": 1,
                "name": "something"
            },
            "default_port": 12201,
            "default_limit": 0,
            "identifier": "PoolTest-2",
        }
    ]

    pool_module.create(pools=pools_to_create)

PUT
***

The List of fields available for update a Server Pool is:

    * id - **Mandatory**
    * identifier - **Mandatory**
    * default_port - **Mandatory**
    * environment - **Mandatory**
    * servicedownaction - **Mandatory**
        * id
        * name - **Mandatory**
    * lb_method - **Mandatory**
    * healthcheck - **Mandatory**
        * identifier - **Mandatory**
        * healthcheck_type - **Mandatory**
        * healthcheck_request - **Mandatory**
        * healthcheck_expect - **Mandatory**
        * destination - **Mandatory**
    * default_limit - **Mandatory**
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
    * server_pool_members - **Mandatory**
        * ipv6 - **Mandatory**
            * id  - **Mandatory**
            * ip_formated - **Mandatory**
        * ip - **Mandatory**
            * id - **Mandatory**
            * ip_formated - **Mandatory**
        * priority - **Mandatory**
        * weight - **Mandatory**
        * limit - **Mandatory**
        * port_real - **Mandatory**
        * member_status - **Mandatory**


Update List of Server Pools
===========================

Here you need to call update() method at pool_module.

You need to pass 1 parameter:
    * **pools**: List containing server pools that you want to update.

Example:

.. code-block:: python

    pools_to_update = [
        {
            "id": 1,
            "lb_method": "least-conn",
            "server_pool_members": [

            ],
            "healthcheck": {
                "healthcheck_type": "TCP",
                "destination": "*:*",
                "healthcheck_expect": "",
                "identifier": "Test_12334",
                "healthcheck_request": ""
            },
            "environment": 449,
            "servicedownaction": {
                "id": 1,
                "name": "something"
            },
            "default_port": 993,
            "default_limit": 0,
            "identifier": "PoolTest-New",
            "users_permissions": [
                {
                    "user": 1,
                    "read": True,
                    "write": False,
                    "delete": False,
                    "change_config": False
                }
            ],
            "groups_permissions": [
                {
                    "user_group": 2,
                    "read": True,
                    "write": False,
                    "delete": False,
                    "change_config": False
                }
            ]
        },
        {
            "id": 2,
            "lb_method": "least-conn",
            "server_pool_members":[
                {
                    "port_real": 554,
                    "weight": 2,
                    "ip": {
                        "ip_formated": "10.134.9.203",
                        "id": 6
                    },
                    "priority": 2,
                    "limit": 0,
                    "member_status": 7,
                    "ipv6": {
                        "ip_formated": "fdbe:fdbe:0000:0000:0000:0000:0000:0002",
                        "id": 3
                    }
                },
                {
                    "port_real": 346,
                    "weight": 1,
                    "ip": {
                        "ip_formated": "10.134.9.205",
                        "id": 7
                    },
                    "priority": 2,
                    "limit": 0,
                    "member_status": 7,
                    "ipv6": {
                        "ip_formated": "fdbe:fdbe:0000:0000:0000:0000:0000:0002",
                        "id": 3
                    }
                }
            ],
            "healthcheck":{
                "healthcheck_type": "HTTP",
                "destination": "*:14500",
                "healthcheck_expect": "",
                "identifier": "Test_8787",
                "healthcheck_request": ""
            },
            "environment": 543,
            "servicedownaction":{
                "id": 1,
                "name": "something"
            },
            "default_port": 12201,
            "default_limit": 0,
            "identifier": "PoolTest-New-2",
        }
    ]

    pool_module.update(pools=pools_to_update)


DELETE
******

Delete List of Server Pools
===========================

Here you need to call delete() method at pool_module.

You need to pass 1 parameter:
    * **ids**: List containing identifiers of server pools that you want to delete.

Example:

.. code-block:: python

    pool_module.delete(ids=[1, 2, 3])

