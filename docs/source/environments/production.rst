Production
==========

The production workflow is the workflow suited to production where no
development takes place and everything runs with maximum automation.
Alternatively this workflow is also applicable to individual developers,
developing on their own computers. This is the production flow implemented at
IMG, IIT Roorkee.

The postulates of the production workflow are:

- **There is the production server.**

  It must be powerful enough to bear the load of all the people who would be
  using it. Depending on your college size and your own purchasing power, that
  could mean your laptops or entire farms.

- **One person, the sysadmin, the boss, the chief, opens an SSH session.**

  I wasn't sure if SSHs or SSHes, so I went with *'...opens an SSH session'*.
  This person must manage an underprivileged user on the server, which still
  has Docker rights though.

  At IMG, we call this user ``apps``. Again you can name it whatever you damn
  well please, provided you remember this name for future use.

- **Everything is managed and orchestrated by Docker Compose.**

  You execute one command and everything goes up.

We are pretty confident that's how any production would work so you should be 
fine. If you are smart enough to use an altogether different production setup, 
you should be smart enough to tweak this to your use. You're on your own for
this one, unfortunately.

Remember our advice from :doc:`the development section <development>`.
