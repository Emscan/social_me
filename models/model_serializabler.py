class Serializabler(object):
	def serializable(self, includes=None, excludes=None, relationships=None):
		result = {}
		columns = includes or self.__table__.columns.keys()

		if excludes:
			columns = [c for c in columns if c not in excludes]
		for column in columns:
			result[column] = self.__dict__[column]
		if relationships:
			for name, rel in relationships.iteritems():
				if not hasattr(self, name):
					continue
				prop = getattr(self, name)
				if isinstance(prop, list):
					result[name] = [r.serializable(**rel) for r in prop]
				else:
					result[name] = prop.serializable(**rel)
		return result
