def tag(name, **kwargs):
    print(name)
    print(kwargs)
    print(type(kwargs))


tag("img", src="Monet.jpg", alt="Sunrise by Claude Monet", border=1)
