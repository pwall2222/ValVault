from pykeepass.entry import Entry as KpEntry


class EntryException(BaseException):
    """Missing or malformed KpEntry when generating custom Entry"""
    pass


class Entry():
    entry: KpEntry
    _username: str = ""
    _password: str = ""
    _alias: str = ""
    _alt: bool = False

    @property
    def alias(self):
        return self._alias

    @alias.setter
    def alias(self, value: str):
        self.set_custom_property("alias", value)
        self._alias = value

    @property
    def alt(self):
        return self._alt

    @alt.setter
    def alt(self, value: bool):
        self.set_custom_property("alt", str(int(value)))
        self._alt = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value: str):
        self.entry.username = value
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value: str):
        self.entry.password = value
        self._password = value

    def set_custom_property(self, key, value):
        self.entry.set_custom_property(key, value)

    def __init__(self, entry):
        try:
            self._extract_entry(entry)
        except AssertionError as e:
            raise EntryException(*e.args) from None
        except ValueError:
            raise EntryException("Alt not an integer") from None

    def _extract_entry(self, entry):
        assert isinstance(entry, KpEntry), "Missing entry"
        assert isinstance(entry.username, str), "Missing username"
        assert isinstance(entry.password, str), "Missing password"
        assert "alias" in entry.custom_properties, "Missing alias"
        assert "alt" in entry.custom_properties, "Missing alt"
        alias = entry.custom_properties["alias"]
        alt = entry.custom_properties["alt"]
        assert isinstance(alias, str), "Bad format alias"
        assert isinstance(alt, str), "Bad format alt"
        self._username = entry.username
        self._password = entry.password
        self._alias = alias
        self._alt = bool(int(alt))
        self.entry = entry

    def __repr__(self) -> str:
        return f"Entry(username={self.username}, alias={self.alias}, alt={self.alt})"
