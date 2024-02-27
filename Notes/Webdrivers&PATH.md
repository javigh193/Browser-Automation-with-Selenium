# Changing geckodriver for Firefox in Ubuntu 22.04

When i tried to instantiate a browser with Selenium, an exception was raised due to the geckodriver available in PATH not being up to date.

First i tried updating and upgrading with apt, but the same problem persisted.

The solution required the following steps:

1. Download the new version of geckodriver for GNU/Linux:

    https://github.com/mozilla/geckodriver/releases

2. Move the driver to the expected directory (PATH):

    sudo mv geckodriver /usr/bin/geckodriver

3. Change owner:

    sudo chown root:root /usr/bin/geckodriver

4. Change permissions:

    sudo chmod +x /usr/bin/geckodriver

Once reached this point, i tried again to instantiate a browser and encountered a different problem. It was impossible to load my Firefox profile. 

Looking around i found a solution that involved uninstalling Firefox and installing it again without snap. But this solution did not please me at all, first of all because it meant that i could not continue using Firefox in my laptop as i used to. 

For the moment i won't be trying to work with Firefox, since it appears to be a problem related to Ubuntu 22.04. 


