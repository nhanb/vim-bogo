#!/usr/bin/env python

# Basically ripped off from Horatio's stackoverflow question
# http://stackoverflow.com/questions/22031653/how-to-change-ibus-input-method-in-python

try:
    import ibus, vim
    bus = ibus.Bus()
    ic = ibus.InputContext(bus, bus.current_input_contxt())
    name = vim.eval("a:name")
    engines = bus.get_engines_by_names([name])
    size = len(engines)
    if size <= 0:
        print "Could not find engine %s" % name
    else:
        engine = engines[0]
    ic.set_engine(engine)

except Exception, e:
    print "Failed to connect to iBus"
    print e
