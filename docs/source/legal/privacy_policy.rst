Privacy policy
==============

This policy explains what Omniport holds about you, why it holds it, who else
can see it and what you can do about it.
It applies to this installation of Omniport, run by the Information Management
Group at the Indian Institute of Technology Roorkee, and to every application
served through it.

Using the portal means this policy applies to you.
It sits alongside the :doc:`developer terms of use <developer_terms_of_use>`,
which binds the people who build applications on top of Omniport.

What Omniport holds
-------------------

Given to Omniport by the institute
++++++++++++++++++++++++++++++++++

Your account exists because the institute enrolled or employed you, and the
records behind it come from the institute rather than from you.

- Your name, your username and the roles you hold, such as student, faculty
  member, maintainer or non-teaching staff, each with the period it is active
  for
- For students, your enrolment number, branch, degree, current year, current
  semester and current CGPA
- For faculty and staff, your department and designation
- Your institute webmail address
- Your allotted residence and room number

Given to Omniport by you
++++++++++++++++++++++++

Some of what Omniport holds is there because you or an application you use put
it there.
None of it is required to sign in.

- Contact details: personal phone numbers, a personal email address and a video
  conferencing identifier
- A display picture, and any files you upload through an application
- An address, including its city, state, postal code and coordinates where you
  supply them
- Links to your profiles on other sites
- Some applications record more than the portal itself needs. Depending on
  which are installed, this can include your date of birth, blood group,
  gender, sex, pronoun and any impairment you declare; your religion and
  reservation category; your passport and driving licence numbers; and
  financial details such as a bank account and annual income

.. warning::

  You can see and change your own financial and political information through
  Settings. Some of it is also visible to the staff who administer the service
  that needs it: the hostel application, for instance, shows a resident's date
  of birth and reservation category to the people managing that hostel.

Produced by your use of the portal
++++++++++++++++++++++++++++++++++

- A session, held while you are signed in, identified by a cookie named
  ``omniport_session``
- Tokens issued to applications you authorise, and the record of which
  applications you have authorised
- An audit trail: when a request is refused for want of permission, or when
  you carry out an operation the portal treats as sensitive, the portal records
  what was attempted, when, and which account attempted it
- Server logs of requests made to the portal

Why Omniport holds it
---------------------

To sign you in and decide what you may see.
Almost everything above exists to answer one of two questions: who are you, and
is this yours to open.

To run the applications you use.
An application asks the portal who you are and what roles you hold, and shows
you what those roles entitle you to.

To keep the portal secure and working.
The audit trail exists so that a refused request or a sensitive operation can
be traced afterwards.
Server logs exist so that failures can be diagnosed.

Omniport does not sell what it holds, does not use it for advertising, and does
not profile you.

Who else can see it
-------------------

Applications you authorise
++++++++++++++++++++++++++

Applications built by others can ask you to sign in with your Omniport account.
When you agree, that application receives the information covered by the
permissions it asked for, and no more.
You are shown what it is asking for before you agree, and you can withdraw a
grant afterwards.

An application that receives your information holds it under its own privacy
policy, which the developer terms of use require it to publish.
IMG does not control what a third-party application does with what you have let
it see.

Maintainers
+++++++++++

The people who run this installation can see what the portal holds, because
somebody has to be able to fix it.

Services Omniport runs on
+++++++++++++++++++++++++

Where this installation is configured to use them, three kinds of external
service can receive information:

- An error reporting service, which receives the details of a failed request,
  and may include the account it was made by
- A search service, which indexes content so that it can be found
- Mail and messaging services, which deliver notifications the portal sends

Nothing else is shared, and nothing is shared for any purpose other than
running the portal.

How long it is kept
-------------------

Server and audit logs are rotated daily and the last 32 days are kept.

Sessions last until you sign out or the session expires.
Tokens issued to applications expire on their own, and a token you revoke stops
working immediately.

Everything else is kept indefinitely.
Leaving the institute ends your access to the portal, but it does not delete
what the portal holds about you, and your enrolment, contact and personal
information stay in the database after you have gone.
If you want something removed, write to us, though whether it can be removed
depends on whether the institute still needs it.

What you can do
---------------

You can see and correct most of what you have given Omniport yourself, through
the portal.

You can see which applications you have authorised, and withdraw any of them.
Withdrawing stops that application receiving anything further; what it already
holds is a matter between you and that application.

Records that come from the institute cannot be changed in the portal, because
the portal is not where they are kept.
Correcting one means correcting it at its source, with the office that holds it.

For anything else, including a request to see what is held about you, to have
something corrected or removed, or to raise a complaint, write to IMG at
img@iitr.ac.in.

Keeping it safe
---------------

Traffic to the portal is encrypted.
Passwords are never stored as text. They are hashed with Argon2.
Access to what the portal holds is decided by your roles, and refusals are
recorded.

No system is perfectly safe, and this one does not claim to be.
If you believe an account or the portal has been compromised, tell IMG at once.

Changes to this policy
----------------------

This policy will change as Omniport changes.
Its history is public, in the repository this documentation is built from, so
what changed and when is a matter of record.

Contacting us
-------------

Write to img@iitr.ac.in, or by post.

::

  INFORMATION MANAGEMENT GROUP,
  INSTITUTE COMPUTER CENTRE,
  INDIAN INSTITUTE OF TECHNOLOGY ROORKEE,
  ROORKEE - 247667, HARIDWAR DISTRICT,
  UTTARAKHAND, INDIA (IN)
  ATTN.: CHIEF COORDINATORS
