## SSH

***SSH*** Stands for ***S***ecure ***SH***ell

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

Key pairs are created through the `ssh-keygen -C` unix command!