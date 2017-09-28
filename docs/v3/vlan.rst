Using Vlan module
#################

Assuming that you have Client Factory instantiated (see :ref:`How to Instantiate Client Factory <client-factory>`) at **client** variable, in order to access methods relative to Vlan module you need to call create_api_vlan() at **client**.

Example:

.. code-block:: python

   vlan_module = client.create_api_vlan()

For more information, please look GloboNetworkAPI documentation.

GET
***

The List of fields available at Vlan module is:

    * id
    * name
    * num_vlan
    * environment
    * description
    * acl_file_name
    * acl_valida
    * acl_file_name_v6
    * acl_valida_v6
    * active
    * vrf
    * acl_draft
    * acl_draft_v6
    * networks_ipv4
    * networks_ipv6
    * vrfs
    * groups_permissions

Obtain List of Vlans through id's
=================================

Here you need to call get() method at vlan_module.

You can pass up to 5 parameters:
    * **ids**: List containing identifiers of vlans.
    * **include**: Array containing fields to include on response.
    * **exclude**: Array containing fields to exclude on response.
    * **fields**: Array containing fields to override default fields.
    * **kind**: string where you can choose between "basic" or "details".

The response will be a dict with a list of Vlans.

Examples:

.. code-block:: python

    vlans = vlan_module.get(ids=[1, 2, 3])

.. code-block:: python

    vlans = vlan_module.get(ids=[1, 2, 3],
                            include=['name', 'vrf'],
                            exclude=['environment'],
                            kind='basic')

.. code-block:: python

    vlans = vlan_module.get(ids=[1, 2, 3],
                            fields=['id', 'name', 'vrf'])

Obtain List of Vlans through extended search
============================================

Here you need to call search() method at vlan_module.

You can pass up to 5 parameters:
    * **search**: Dict containing QuerySets to find vlans.
    * **include**: Array containing fields to include on response.
    * **exclude**: Array containing fields to exclude on response.
    * **fields**: Array containing fields to override default fields.
    * **kind**: string where you can choose between "basic" or "details".

The response will be a dict with a list of Vlans.

Example:

.. code-block:: python

    search = {'extends_search': [{'num_vlan': 1}],
              'start_record': 0,
              'custom_search': '',
              'end_record': 25,
              'asorting_cols': [],
              'searchable_columns': []}
    fields = ['id', 'name']

    vlans = vlan_module.search(search=search, fields=fields)

POST
****

The List of fields available for create a Vlan is:

    * name - **Mandatory**
    * num_vlan
    * environment - **Mandatory**
    * acl_file_name
    * acl_file_name_v6
    * acl_valida
    * acl_valida_v6
    * active
    * vrf
    * acl_draft
    * acl_draft_v6
    * create_networkv4
        * network_type
        * environmentvip
        * prefix
    * create_networkv6
        * network_type
        * environmentvip
        * prefix

Create List of Vlans
====================

Here you need to call create() method at vlan_module.

You need to pass 1 parameter:
    * **vlans**: List containing vlans that you want to create.

Example:

.. code-block:: python

    vlans_to_create = [
        {
            "name": "Vlan 1",
            "num_vlan": 3,
            "environment": 5,
            "active": True,
            "create_networkv4": {
                "network_type": 6,
                "environmentvip": 2,
                "prefix": 24
            }
        },
        {
            "name": "Vlan 2",
            "num_vlan": 4,
            "environment": 10,
            "active": True,
            "create_networkv4": {
                "network_type": 6,
                "environmentvip": 3,
                "prefix": 24
            }
        }
    ]

    vlan_module.create(vlans=vlans_to_create)


PUT
***

The List of fields available for update a Vlan is:

    * id - **Mandatory**
    * name - **Mandatory**
    * num_vlan - **Mandatory**
    * environment - **Mandatory**
    * description - **Mandatory**
    * acl_file_name - **Mandatory**
    * acl_valida - **Mandatory**
    * acl_file_name_v6 - **Mandatory**
    * acl_valida_v6 - **Mandatory**
    * active - **Mandatory**
    * vrf - **Mandatory**
    * acl_draft - **Mandatory**
    * acl_draft_v6 - **Mandatory**

Update List of Vlans
====================

Here you need to call update() method at vlan_module.

You need to pass 1 parameter:
    * **vlans**: List containing vlans that you want to update.

Example:

.. code-block:: python

    vlans_to_update = [
        {
            "id": 1,
            "name": "Vlan 1 changed",
            "num_vlan": 3,
            "environment": 5,
            "description": "",
            "acl_file_name": "",
            "acl_valida": false ,
            "acl_file_name_v6": "",
            "acl_valida_v6": false,
            "active": false,
            "vrf": 'VrfTest',
            "acl_draft": "",
            "acl_draft_v6": ""
        },
        {
            "id": 2,
            "name": "Vlan changed",
            "num_vlan": 4,
            "environment": 10,
            "description": "",
            "acl_file_name": "",
            "acl_valida": false ,
            "acl_file_name_v6": "",
            "acl_valida_v6": false,
            "active": false,
            "vrf": 'VrfTest',
            "acl_draft": "",
            "acl_draft_v6": ""
        }
    ]

    vlan_module.update(vlans=vlans_to_update)

DELETE
******

Delete List of Vlans
====================

Here you need to call delete() method at vlan_module.

You need to pass 1 parameter:
    * **ids**: List containing identifiers of vlans that you want to delete.

Example:

.. code-block:: python

    vlan_module.delete(ids=[1, 2, 3])

