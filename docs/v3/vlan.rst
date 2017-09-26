Using Vlan module
#################

Assuming that you have Client Factory instantiated (see :ref:`How to Instantiate Client Factory <client-factory>`) at client variable, in order to access methods relative to Vlan module you need to call
create_api_vlan() at client.

Example:
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

    Here you need to use get() function.

    You can pass up to 5 parameters:
        ids: List containing identifiers of vlans.
        include: Array containing fields to include on response.
        exclude: Array containing fields to exclude on response.
        fields: Array containing fields to override default fields.
        kind: string where you can choose between "basic" or "details".

    The response will be dict with a list of Vlans

    Example:

Obtain List of Vlans through extended search
============================================

    Here you need to use search() function.

    You can pass up to 5 parameters:
        search: Dict containing QuerySets to find vlans.
        include: Array containing fields to include on response.
        exclude: Array containing fields to exclude on response.
        fields: Array containing fields to override default fields.
        kind: string where you can choose between "basic" or "details".

    The response will be dict with a list of Vlans

    Example:


POST
****

Create List of Vlans
====================

    Here you need to use create() function.

    You need to pass 1 parameter:
        vlans: List containing vlans that you want to create.

    Example:

PUT
***

Update List of Vlans
====================

    Here you need to use update() function.

    You need to pass 1 parameter:
        vlans: List containing vlans that you want to update.

    Example:

DELETE
******

Delete List of Vlans
====================

    Here you need to use delete() function.

    You need to pass 1 parameter:
        ids: List containing identifiers of vlans that you want to delete.

    Example:

