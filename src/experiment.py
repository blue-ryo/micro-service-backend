class HelloWorld:
  def __init__(self, name: str):
    self._name = name

  def echo(self):
    print(f"Hello {self._name}!")


if __name__ == "__main__":
  hello = HelloWorld("Kota")
  hello.echo()

