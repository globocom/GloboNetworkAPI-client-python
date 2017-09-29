Using AS module
###############

Assuming that you have Client Factory instantiated (see :ref:`How to Instantiate Client Factory <client-factory>`) at **client** variable, in order to access methods relative to AS module you need to call create_api_v4_as() at **client**.

Example:

.. code-block:: python

   ans_module = client.create_api_v4_as()

For more information, please look GloboNetworkAPI documentation.

GET
***

The List of fields available at AS module is:

    * id
    * name
    * description
    * equipments

Obtain List of ASNs through id's
================================

Here you need to call get() method at ans_module.

You can pass up to 5 parameters:
    * **ids**: List containing identifiers of ASNs.
    * **include**: Array containing fields to include on response.
    * **exclude**: Array containing fields to exclude on response.
    * **fields**: Array containing fields to override default fields.
    * **kind**: string where you can choose between "basic" or "details".

The response will be a dict with a list of ASNs.

Examples:

.. code-block:: python

    asns = ans_module.get(ids=[1, 2, 3])

.. code-block:: python

    asns = ans_module.get(ids=[1, 2, 3],
                          kind='basic')

.. code-block:: python

    asns = ans_module.get(ids=[1, 2, 3],
                          fields=['id', 'name'])

Obtain List of ASNs through extended search
===========================================

Here you need to call search() method at ans_module.

You can pass up to 5 parameters:
    * **search**: Dict containing QuerySets to find ASNs.
    * **include**: Array containing fields to include on response.
    * **exclude**: Array containing fields to exclude on response.
    * **fields**: Array containing fields to override default fields.
    * **kind**: string where you can choose between "basic" or "details".

The response will be a dict with a list of ASNs.

Example:

.. code-block:: python

    search = {
        'extends_search': [{
            "name": "AS_BGP"
        }],
        'start_record': 0,
        'custom_search': '',
        'end_record': 25,
        'asorting_cols': [],
        'searchable_columns': []}
    fields = ['id', 'name']

    asns = ans_module.search(search=search, fields=fields)

POST
****

The List of fields available for create an AS is:

    * name - **Mandatory**
    * description - **Mandatory**

Create List of ASNs
===================

Here you need to call create() method at ans_module.

You need to pass 1 parameter:
    * **asns**: List containing ASNs that you want to create.

Example:

.. code-block:: python

    asns_to_create = [
        {
            "name": "11",
            "descripton": "AS-11"
        },
        {
            "name": "12",
            "descripton": "AS-12"
        }
    ]

    ans_module.create(asns=asns_to_create)


PUT
***

The List of fields available for update an AS is:

    * id - **Mandatory**
    * name - **Mandatory**
    * description - **Mandatory**

Update List of ASNs
===================

Here you need to call update() method at ans_module.

You need to pass 1 parameter:
    * **asns**: List containing ASNs that you want to update.

Example:

.. code-block:: python

    asns_to_update = [
        {
            "id": 1,
            "name": "13",
            "descripton": "AS-13"
        },
        {
            "id": 2,
            "name": "14",
            "descripton": "AS-14"
        }
    ]

    ans_module.update(asns=asns_to_update)


DELETE
******

Delete List of ASNs
===================

Here you need to call delete() method at ans_module.

You need to pass 1 parameter:
    * **ids**: List containing identifiers of ASNs that you want to delete.

Example:

.. code-block:: python

    ans_module.delete(ids=[1, 2, 3])

