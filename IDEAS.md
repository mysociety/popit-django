# Ideas for future features

For the active work please see the [issues
list](https://github.com/mysociety/popit-django/issues?state=open).

## Data model

  * Document how to add fields to the ones defined in the `popit` `models.py`
    classes. What is the best approach to extending them?

## Syncing

  * Mark some `popit.model.ApiInstance` entries as local only so that they are
    ignored when syncing to remote APIs.

  * Fetch organisations, posts and memberships. Create the correct foreign key
    relationships for them.

  * Fetch and store sub documents such as contact details, etc. For sub
    documents that can be found in several top level document classes should a
    `ContactDetailBase` class be created that is then used to create
    `PersonContactDetail` with a simple foreign key be used, or should we use
    the [content
    types](https://docs.djangoproject.com/en/dev/ref/contrib/contenttypes/)
    framework?

  * Handle deletes from the API elegantly - the API should return `410 Gone` for
    deleted documents rather than `404 Not Found`. Some thought will be required
    as to how best to handle this locally - just doing a cascading delete of all
    related entries is probably the wrong approach. Requires changes to the
    popit-api codebase.

  * Track last sync time and use it to only fetch changes (creates, updates and
    deletes) since that time. Requires changes to the popit-api codebase.

  * Allow local data to be written out to a PopIt-API. Could be implemented as a
    one-off export tool with the local records being changed to reflect that
    they are now from a remote API.


## Admin

  * Allow individual records to be updated on demand from the admin pages.

  * The admin could be made smart to allow editing of local data that is not
    backed by a PopIt instance.

  * Once the main PopIt client side editing interface for the API is finished it
    might be possible to embed it in this app so that you could directly edit
    the PopIt-API and then sync the changes. Or at least link from the admin to
    the editing interface for the API.

