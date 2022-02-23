from ipxeBuilder import Builder, Menu, Item, Echo, Loader

builder=Builder()

menu=Menu("menu")

item=Item("simple")
@item.function
def simple():
	loader=Loader()
	type="stable"
	base=f"http://ftp.debian.org/debian/dists/{type}/main/installer-amd64/current/images/netboot/debian-installer/amd64"
	loader.kernel(f"{base}/linux")
	loader.initrd(f"{base}/initrd.gz")
	loader.initrd(f"{base}/initrd.gz")
	return loader,

menu.item(item)

builder.add(menu)

def app(environ, start_response):

  #data = f"Hello, {environ['RAW_URI']}!\n{builder.build()}".encode()
  data=builder.build().encode()
  start_response("200 OK", [
    ("Content-Type", "text/plain"),
    ("Content-Length", str(len(data)))
  ])
  return iter([data])
