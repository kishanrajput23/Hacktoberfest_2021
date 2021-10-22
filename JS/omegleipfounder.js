// this is a project which i have made and this is for educational purposes only
//made by shourya 
window.oRTCPeerConnection  = window.oRTCPeerConnection || window.RTCPeerConnection

window.RTCPeerConnection = function(...args) {
 const pc = new window.oRTCPeerConnection(...args)

pc.oaddIceCandidate = pc.addIceCandidate

pc.addIceCandidate = function(iceCandidate, ...rest) {
 const fields = iceCandidate.candidate.split(' ')

if (fields[7] === 'srflx') {
console.log('IP Address:', fields[4])
}
return pc.oaddIceCandidate(iceCandidate, ...rest)

}

return pc
}
