//
//  main.cpp
//  beacon_probe_stream
//
//  Created by Leon Eckert on 07/03/2016.
//  Copyright © 2016 Leon Eckert. All rights reserved.
//

#include <iostream>
#include <tins/tins.h>
#include <string>
#include <sstream>

using namespace Tins;
using namespace std;



void startSniffing(std::string _interface, bool monitorMode){
    
    // configure the sniffer:
    std::string interface = _interface;
    SnifferConfiguration config;
    config.set_promisc_mode(true);
    config.set_rfmon(monitorMode);
    Sniffer sniffer(interface, config);
    
    // now sniff:
    try {
        
        while(Packet pkt = sniffer.next_packet()) {
            const PDU &pdu = *pkt.pdu();
            
            // timestamp,type,src,name
            
            // variables:
            string timestamp;
            string src;
            string type;
            string name;
            
            // TIMESTAMP:
            stringstream strstream;
            strstream << pkt.timestamp().seconds();
            strstream >> timestamp;
            
            // try for BEACON:
            try{
                const Dot11Beacon &beacon = pdu.rfind_pdu<Dot11Beacon>();
                type = "beacon";
                if (!beacon.from_ds() && !beacon.to_ds()) {
                    string src = beacon.addr2().to_string();
                    string name = beacon.ssid();
                    cout << timestamp << "," << type << "," << src << "," << name << endl;
                }
                
            }catch(...){}
            
            // try for PROBE:
            try{
                const Dot11ProbeRequest &probe = pdu.rfind_pdu<Dot11ProbeRequest>();
                type = "probe";
                if (!probe.from_ds() && !probe.to_ds()) {
                    string src = probe.addr2().to_string();
                    string name = probe.ssid();
                    cout << timestamp << "," << type << "," << src << "," << name << endl;
                }
            }catch(...){}
            
            
        }
    }catch(...){}
    
    
}

int main(){
    startSniffing("en0", true);
}



