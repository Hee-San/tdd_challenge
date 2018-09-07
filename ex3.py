import re

class Address:
    def __init__(self, _input, _output):
        self._input = _input
        self._output = _output

    def validate_addr_spec(self):
        addresses = self._input.read().split('\n')
        addresses = addresses[0:-1]
        for address in addresses:
            if re.fullmatch(r'[^@]*@[^@]*', address):
                self._output.write("ok")
            else:
                self._output.write("ng")
            

