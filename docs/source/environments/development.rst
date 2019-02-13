Development
===========

The development workflow is the workflow suited to teams where multiple
developers work on multiple projects at the same time. This is the development
flow implemented at IMG, IIT Roorkee.

The postulates of the development workflow are:

- **There is a central development server.**
    
  It must be highly powerful, but it depends on how many developers are 
  going to be simultaneously developing on and for Omniport.

- **Developers SSH into the remote from a terminal in the maintainers' lab.**
    
  Each developer gets a unique account on the remote. They clone the codebase
  (and not the infrastructure) in their accounts, each running a copy and 
  making their changes in said copy.

  All development work happens on the remote. One feasible option is 
  programming on Vim inside SSH. Another is programming on the codebase 
  replicated via SFTP.

- **Application servers share standalone services.**
    
  The common services such as the database and the message-broker are run in
  the Docker sandbox under an altogether different user, which is neither the
  ``root``, nor one of the developers.

  At IMG we call this user ``apps``. You are free to name it whatever pleases
  you. Just remember this name for later.

- **All developers run their own application servers.**
    
  Since application servers hot-load the code from the host, every developer
  can host their code independently of other application servers.

- **Application servers expose a port on the 0.0.0.0 interface on the server.**
    
  The Django development server runs on ``0.0.0.0:600xx`` and the React
  development server runs on ``0.0.0.0:610xx``, proxying requests to the 
  Django server.
    
  These servers can be accessed in a browser on the developer's local terminal
  by visiting ``http://<server_IP>:<port>/``.
    
If this is not your setup and you are not in a postition for this to be your 
setup, you are, unfortunately, on your own for this one. See if our production
setup suits you more, but that's about as far as we can go.

But given that you are developers, we have complete faith that you'll find a 
way. *Developers always do.*