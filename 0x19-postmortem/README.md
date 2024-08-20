Timeline

-August 15, 14:00 UTC: Issue detected when I attempted to SSH into my server and got an “Access Denied” message.
- August 15, 14:30 UTC: After multiple failed attempts, I started suspecting something was wrong beyond a typo.
- August 15, 15:00 UTC: I reviewed the project documentation, assuming I missed a step, but it didn't provide a solution.
- August 15, 16:00 UTC: I attended an SSH workshop with mentors, hoping to find a clue. Felt like I was getting closer, but no success.
- August 16, 10:00 UTC:Spent hours Googling and reading Stack Overflow posts. Every solution I tried just deepened my despair.
- August 17, 08:00 UTC: Missed the second project deadline. This was a low point.
- August 18, 09:00 UTC: Escalated the issue to mentors and peers in the ALX community, hoping for fresh perspectives.
- August 18, 18:00 UTC: A mentor suggested a combination of resetting my SSH keys and double-checking firewall settings.
- August 18, 22:00 UTC:Finally, successfully connected to the server using the combination of techniques learned from the workshop, Google searches, and mentor advice.


Root Cause and Resolution

Root Cause: 
The primary issue was an SSH configuration error, specifically related to incorrect key permissions and a firewall rule blocking the connection. Complicating matters, I relied on an outdated tutorial that led me down a rabbit hole of incorrect assumptions.

Resolution:
The problem was resolved by resetting the SSH keys, adjusting the key permissions (`chmod 600` for the private key), and updating the firewall settings to allow SSH traffic. The final breakthrough came after applying the layered knowledge from the SSH workshop and community feedback.


Corrective and Preventative Measures

Improvements:

-Documentation Review: Ensure that I’m using up-to-date and reliable sources when troubleshooting.
-Community Engagement: Earlier engagement with mentors and peers could have saved a lot of time and stress.
-Practical Workshops: More hands-on practice with SSH and server configuration could have prevented the error.

Tasks:
1.Update Documentation: Review and update the internal documentation to reflect the latest SSH configuration best practices.
2.Implement Monitoring: Add monitoring for SSH connection attempts and firewall settings to catch similar issues earlier.
3.Practice SSH: Schedule regular practice sessions for SSH and server configuration to stay sharp.
4. Set Up Alerts: Configure alerts for missed project deadlines to prompt early escalation and prevent repeat scenarios.


Despite the stress and frustration, this experience was a valuable lesson in perseverance, the importance of asking for help, and the benefits of a well-rounded troubleshooting strategy. And hey, at least I now have an impressive SSH battle story!

