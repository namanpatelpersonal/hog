import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)

