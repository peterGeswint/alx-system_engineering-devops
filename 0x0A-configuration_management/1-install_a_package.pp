#!/usr/bin/pup
# Install flask v2.1.0
package {'flask':
	ensure	=> '2.1.0',
	provider=> 'pip'

}

