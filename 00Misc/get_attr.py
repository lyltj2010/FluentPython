"""
getattr
    * Return the value of the named attribute of object.
    * For example, getattr(x, 'foobar') is equivalent to x.foobar
    * If the named attribute does not exist, default is returned if provided
    * otherwise AttributeError is raised
Ref
    * http://www.diveintopython.net/power_of_introspection/getattr.html

>>> li = ["Larry", "Curly"]
>>> getattr(li, "append")("Moe")
>>> li
['Larry', 'Curly', 'Moe']

A common usage pattern of getattr is as a dispatcher
    * Use only one dispatch function
    * If new function like output_pdf added, you don't need edit your core code
>>> def output(data, format="txt"):
...     output_function = getattr(Outputter, "output_%s" % format, Outputter.output_txt)
...     return output_function(data)
>>> output('Hi')
<txt>Hi</txt>
>>> output('Hi', format='html')
<html>Hi</html>
"""

class Outputter():
    @classmethod
    def output_txt(cls, data):
        print('<txt>%s</txt>' % data)

    @classmethod
    def output_html(cls, data):
        print('<html>%s</html>' % data)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
