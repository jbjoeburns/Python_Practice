## SSH

***SSH*** Stands for ***S***ecure ***SH***ell

Good for automation...

What is it?:
- SSH is a communication protocol to allow computers to communicate securely and alter/transfer eachother's files.
  - Used it during project when I was connecting to compute clusters, I think it's a linux command `ssh <login details>`

Private vs public keys:
- Keys used to connect, private key is sent out and public key is sent back to prove users identity and server identity respectively
- Private key stays with the user (and only there), while the public key is sent to the server.

How does SSH increase security?:
- All communication is encrypted
- Requires key to access remote server, functionally a password
- Ensures not just anyone can connect, or view what the client is doing on the server or the server contents

`cd` to take you to the root directory

then mkdir .ssh to make new ssh hidden directory (see it with ls -a)

Key pairs are created through the `ssh-keygen -C` unix command!
We will use `ssh-keygen -t rsa -b 4096 -C "<email>"`

use `eval 'ssh-agent'` whenever you open pycharm from now on

`ssh-add ~/.ssh/github_test` to access 