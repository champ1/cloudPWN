
import core.config

def self_info(ip):
	config = core.config.get_config()
	return {'iid' : ip,
			'key' : config['self_key'],
			'ip' : ip,
			'tags' : 'Self Hosted system at %s' % ip}