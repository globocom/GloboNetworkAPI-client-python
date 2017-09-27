Using Environment module
########################

Assuming that you have Client Factory instantiated (see :ref:`How to Instantiate Client Factory <client-factory>`) at **client** variable, in order to access methods relative to Environment module you need to call create_api_environment() at **client**.

Example:

.. code-block:: python

   env_module = client.create_api_environment()

For more information, please look GloboNetworkAPI documentation.

GET
***

The List of fields available at Environment module is:

    * id
    * name
    * grupo_l3
    * ambiente_logico
    * divisao_dc
    * filter
    * acl_path
    * ipv4_template
    * ipv6_template
    * link
    * min_num_vlan_1
    * max_num_vlan_1
    * min_num_vlan_2
    * max_num_vlan_2
    * vrf
    * default_vrf
    * father_environment
    * children
    * configs
    * routers
    * equipments
    * sdn_controllers

Obtain List of Environments through id's
========================================

Here you need to call get() method at env_module.

You can pass up to 5 parameters:
    * **ids**: List containing identifiers of environments.
    * **include**: Array containing fields to include on response.
    * **exclude**: Array containing fields to exclude on response.
    * **fields**: Array containing fields to override default fields.
    * **kind**: string where you can choose between "basic" or "details".

The response will be a dict with a list of Environments.

Examples:

.. code-block:: python

    envs = env_module.get(ids=[1, 2, 3])

.. code-block:: python

    envs = env_module.get(ids=[1, 2, 3],
                          include=['name', 'divisao_dc'],
                          exclude=['id'],
                          kind='details')

.. code-block:: python

    envs = env_module.get(ids=[1, 2, 3],
                          fields=['id', 'name', 'grupo_l3'])

Obtain List of Environments through extended search
===================================================

Here you need to call search() method at env_module.

You can pass up to 5 parameters:
    * **search**: Dict containing QuerySets to find environments.
    * **include**: Array containing fields to include on response.
    * **exclude**: Array containing fields to exclude on response.
    * **fields**: Array containing fields to override default fields.
    * **kind**: string where you can choose between "basic" or "details".

The response will be a dict with a list of Environments.

Example:

.. code-block:: python

    search = {
        'extends_search': [{
            'divisao_dc': 1,
            'ambiente_logico__nome': 'AmbLog'
        }],
        'start_record': 0,
        'custom_search': '',
        'end_record': 25,
        'asorting_cols': [],
        'searchable_columns': []}
    fields = ['id', 'name']

    envs = env_module.search(search=search, fields=fields)

POST
****

The List of fields available for create an Environment is:

    * grupo_l3 - **Mandatory**
    * ambiente_logico - **Mandatory**
    * divisao_dc - **Mandatory**
    * filter
    * min_num_vlan_1
    * max_num_vlan_1
    * min_num_vlan_2
    * max_num_vlan_2
    * ipv4_template
    * ipv6_template
    * link
    * acl_path
    * vrf
    * father_environment
    * default_vrf - **Mandatory**
    * configs
        * subnet
        * new_prefix
        * type
        * network_type

Create List of Environments
===========================

Here you need to call create() method at env_module.

You need to pass 1 parameter:
    * **environments**: List containing environments that you want to create.

Example:

.. code-block:: python

    envs_to_create = [
        {
            "grupo_l3": 1,
            "ambiente_logico": 2,
            "divisao_dc": 3,
            "default_vrf": 1
        },
        {
            "grupo_l3": 1,
            "ambiente_logico": 2,
            "divisao_dc": 4,
            "default_vrf": 1,
            "configs": [
                {
                    'subnet': 'febe:bebe:bebe:8200:0:0:0:0/57',
                    'new_prefix': '64',
                    'type': 'v6',
                    'network_type': 8
                },
                {
                    'subnet': '10.10.0.0/16',
                    'new_prefix': '24',
                    'type': 'v4',
                    'network_type': 8
                }
            ]
        }
    ]

    env_module.create(environments=envs_to_create)


PUT
***

Update List of Environments
===========================

Here you need to call update() method at env_module.

You need to pass 1 parameter:
    * **environments**: List containing environments that you want to update.

Example:

.. code-block:: python

    envs_to_update = [
        {
            "id": 1,
            "grupo_l3": 1,
            "ambiente_logico": 2,
            "default_vrf": 1,
            "divisao_dc": 3
        },
        {
            "id": 2,
            "grupo_l3": 1,
            "ambiente_logico": 2,
            "divisao_dc": 4,
            "default_vrf": 1,
            "configs": [
                {
                    'subnet': 'febe:bebe:bebe:8200:0:0:0:0/57',
                    'new_prefix': '64',
                    'type': 'v6',
                    'network_type': 8
                },
                {
                    'subnet': '10.10.0.0/16',
                    'new_prefix': '24',
                    'type': 'v4',
                    'network_type': 8
                }
            ]
        }
    ]

    env_module.update(environments=envs_to_update)


DELETE
******

Delete List of Environments
===========================

Here you need to call delete() method at env_module.

You need to pass 1 parameter:
    * **ids**: List containing identifiers of environments that you want to delete.

Example:

.. code-block:: python

    env_module.delete(ids=[1, 2, 3])

