**verbose_name**

**Options.verbose_name**

A human-readable name for the object, singular:

**verbose_name = "url"**

ex.

slug = models.SlugField(max_length=256, verbose_name='url', unique=True)

If this isn’t given, Django will use a munged version of the class name: **CamelCase** becomes **camel case**.