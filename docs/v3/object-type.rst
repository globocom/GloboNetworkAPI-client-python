Using Object Type module
########################

Assuming that you have Client Factory instantiated (see :ref:`How to Instantiate Client Factory <client-factory>`) at **client** variable, in order to access methods relative to Object Type module you need to call create_api_object_type() at **client**.

Example:

.. code-block:: python

   ot_module = client.create_api_object_type()

For more information, please look GloboNetworkAPI documentation.

GET
***

The List of fields available at Object Type module is:

    * id
    * name

Obtain List of Object Types through id's
====================================================

Here you need to call get() method at ot_module.

You can pass up to 5 parameters:
    * **ids**: List containing identifiers of Object Types.
    * **include**: Array containing fields to include on response.
    * **exclude**: Array containing fields to exclude on response.
    * **fields**: Array containing fields to override default fields.
    * **kind**: string where you can choose between "basic" or "details".

The response will be a dict with a list of Object Types.

Examples:

.. code-block:: python

    ots = ot_module.get(ids=[1, 2, 3])

Obtain List of Object Types through extended search
===============================================================

Here you need to call search() method at ot_module.

You can pass up to 5 parameters:
    * **search**: Dict containing QuerySets to find Object Types.
    * **include**: Array containing fields to include on response.
    * **exclude**: Array containing fields to exclude on response.
    * **fields**: Array containing fields to override default fields.
    * **kind**: string where you can choose between "basic" or "details".

The response will be a dict with a list of Object Types.

Example:

.. code-block:: python

    search = {
        'extends_search': [{
            "name": "Vrf"
        }],
        'start_record': 0,
        'custom_search': '',
        'end_record': 25,
        'asorting_cols': [],
        'searchable_columns': []}
    fields = ['id', 'name']

    ots = ot_module.search(search=search, fields=fields)
