# Python-Interactive-Maps
<!DOCTYPE html>
<head>    
    <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
    
        <script>
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        </script>
    
    <script src="https://cdn.jsdelivr.net/npm/leaflet@1.6.0/dist/leaflet.js"></script>
    <script src="https://code.jquery.com/jquery-1.12.4.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.6.0/dist/leaflet.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css"/>
    <link rel="stylesheet" href="https://rawcdn.githack.com/python-visualization/folium/master/folium/templates/leaflet.awesome.rotate.css"/>
    <style>html, body {width: 100%;height: 100%;margin: 0;padding: 0;}</style>
    <style>#map {position:absolute;top:0;bottom:0;right:0;left:0;}</style>
    
            <meta name="viewport" content="width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
            <style>
                #map_091ff95239d4416db69d4a910d91c640 {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
            </style>
        
    <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.1.0/leaflet.markercluster.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.1.0/MarkerCluster.css"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet.markercluster/1.1.0/MarkerCluster.Default.css"/>
</head>
<body>    
    
            <div class="folium-map" id="map_091ff95239d4416db69d4a910d91c640" ></div>
        
</body>
<script>    
    
            var map_091ff95239d4416db69d4a910d91c640 = L.map(
                "map_091ff95239d4416db69d4a910d91c640",
                {
                    center: [33.75, -84.33],
                    crs: L.CRS.EPSG3857,
                    zoom: 10,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );

            

        
    
            var tile_layer_912ea450524a4bee994dd2313e7c2add = L.tileLayer(
                "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                {"attribution": "Data by \u0026copy; \u003ca href=\"http://openstreetmap.org\"\u003eOpenStreetMap\u003c/a\u003e, under \u003ca href=\"http://www.openstreetmap.org/copyright\"\u003eODbL\u003c/a\u003e.", "detectRetina": false, "maxNativeZoom": 18, "maxZoom": 18, "minZoom": 0, "noWrap": false, "opacity": 1, "subdomains": "abc", "tms": false}
            ).addTo(map_091ff95239d4416db69d4a910d91c640);
        
    
            var marker_cluster_7285d904a9fd4e188799aa89de9be8c0 = L.markerClusterGroup(
                {}
            );
            map_091ff95239d4416db69d4a910d91c640.addLayer(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var marker_587d496bc7874ec688c47f504e53b2bf = L.marker(
                [33.760538145529196, -84.38655546480409],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_30beeaa98005405a9cd52cb1d2b964d4 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_587d496bc7874ec688c47f504e53b2bf.setIcon(icon_30beeaa98005405a9cd52cb1d2b964d4);
        
    
        var popup_688f8abee1774b1ea5e00a35d171c8d6 = L.popup({"maxWidth": "100%"});

        
            var html_d6ae6317432346119f428925d2c86446 = $(`<div id="html_d6ae6317432346119f428925d2c86446" style="width: 100.0%; height: 100.0%;">Rating:5.0</div>`)[0];
            popup_688f8abee1774b1ea5e00a35d171c8d6.setContent(html_d6ae6317432346119f428925d2c86446);
        

        marker_587d496bc7874ec688c47f504e53b2bf.bindPopup(popup_688f8abee1774b1ea5e00a35d171c8d6)
        ;

        
    
    
            marker_587d496bc7874ec688c47f504e53b2bf.bindTooltip(
                `<div>
                     Aviva by Kameel
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_4cfe71e482ab442c8ce5171b62a08e2d = L.marker(
                [34.089366, -84.27497840000001],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_494d8d4616344c419cad88998482c0c0 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_4cfe71e482ab442c8ce5171b62a08e2d.setIcon(icon_494d8d4616344c419cad88998482c0c0);
        
    
        var popup_502009b9237544cc99b325016f5786f1 = L.popup({"maxWidth": "100%"});

        
            var html_13b94b4048454a0fbc5cb0da495b64e6 = $(`<div id="html_13b94b4048454a0fbc5cb0da495b64e6" style="width: 100.0%; height: 100.0%;">Rating:5.0</div>`)[0];
            popup_502009b9237544cc99b325016f5786f1.setContent(html_13b94b4048454a0fbc5cb0da495b64e6);
        

        marker_4cfe71e482ab442c8ce5171b62a08e2d.bindPopup(popup_502009b9237544cc99b325016f5786f1)
        ;

        
    
    
            marker_4cfe71e482ab442c8ce5171b62a08e2d.bindTooltip(
                `<div>
                     Local Expedition Wood Fired Grill
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_3415c9737aff4e3bbba33c4763e45ba6 = L.marker(
                [34.005762, -84.603604],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_00c0f18cb78d448cbfab3a75e6992e53 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_3415c9737aff4e3bbba33c4763e45ba6.setIcon(icon_00c0f18cb78d448cbfab3a75e6992e53);
        
    
        var popup_64e73c67da0647028e738569323ac740 = L.popup({"maxWidth": "100%"});

        
            var html_1f4b2df57eb6433e958dc1d663e6d6fe = $(`<div id="html_1f4b2df57eb6433e958dc1d663e6d6fe" style="width: 100.0%; height: 100.0%;">Rating:5.0</div>`)[0];
            popup_64e73c67da0647028e738569323ac740.setContent(html_1f4b2df57eb6433e958dc1d663e6d6fe);
        

        marker_3415c9737aff4e3bbba33c4763e45ba6.bindPopup(popup_64e73c67da0647028e738569323ac740)
        ;

        
    
    
            marker_3415c9737aff4e3bbba33c4763e45ba6.bindTooltip(
                `<div>
                     Tacos Del Chavo
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_72ad0c75fbc3436bbb0836eb44294050 = L.marker(
                [33.74075, -84.34672990000001],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_6e941b678120424faacac45bae9b4934 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_72ad0c75fbc3436bbb0836eb44294050.setIcon(icon_6e941b678120424faacac45bae9b4934);
        
    
        var popup_5a0f98489c9c4d3f9a4cf8044fbaeb5b = L.popup({"maxWidth": "100%"});

        
            var html_988e43b6d6354de796053a21f2cef878 = $(`<div id="html_988e43b6d6354de796053a21f2cef878" style="width: 100.0%; height: 100.0%;">Rating:5.0</div>`)[0];
            popup_5a0f98489c9c4d3f9a4cf8044fbaeb5b.setContent(html_988e43b6d6354de796053a21f2cef878);
        

        marker_72ad0c75fbc3436bbb0836eb44294050.bindPopup(popup_5a0f98489c9c4d3f9a4cf8044fbaeb5b)
        ;

        
    
    
            marker_72ad0c75fbc3436bbb0836eb44294050.bindTooltip(
                `<div>
                     Marrakech Express
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_57b98d5e04c94e04b1bb72ec7485a595 = L.marker(
                [34.0753984, -84.29597640000001],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_d66b1432b4994d97ad03bac7ae25d33d = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_57b98d5e04c94e04b1bb72ec7485a595.setIcon(icon_d66b1432b4994d97ad03bac7ae25d33d);
        
    
        var popup_829baf9247604efeb3d4613ec8f92210 = L.popup({"maxWidth": "100%"});

        
            var html_a749bcbe8fbb46dbbdc8df9246c5eb7a = $(`<div id="html_a749bcbe8fbb46dbbdc8df9246c5eb7a" style="width: 100.0%; height: 100.0%;">Rating:5.0</div>`)[0];
            popup_829baf9247604efeb3d4613ec8f92210.setContent(html_a749bcbe8fbb46dbbdc8df9246c5eb7a);
        

        marker_57b98d5e04c94e04b1bb72ec7485a595.bindPopup(popup_829baf9247604efeb3d4613ec8f92210)
        ;

        
    
    
            marker_57b98d5e04c94e04b1bb72ec7485a595.bindTooltip(
                `<div>
                     Valor Coffee
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_a5c498cda47842039ff5ccb4f177d440 = L.marker(
                [33.891135, -84.504663],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_ac0d3e6216e94f18a70879aecb542cd2 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_a5c498cda47842039ff5ccb4f177d440.setIcon(icon_ac0d3e6216e94f18a70879aecb542cd2);
        
    
        var popup_8994cf780cad4918a93dd0d99ae83788 = L.popup({"maxWidth": "100%"});

        
            var html_f7105bb0aaee45d9b624ac2d04dddaa4 = $(`<div id="html_f7105bb0aaee45d9b624ac2d04dddaa4" style="width: 100.0%; height: 100.0%;">Rating:5.0</div>`)[0];
            popup_8994cf780cad4918a93dd0d99ae83788.setContent(html_f7105bb0aaee45d9b624ac2d04dddaa4);
        

        marker_a5c498cda47842039ff5ccb4f177d440.bindPopup(popup_8994cf780cad4918a93dd0d99ae83788)
        ;

        
    
    
            marker_a5c498cda47842039ff5ccb4f177d440.bindTooltip(
                `<div>
                     Himalayan Kitchen
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_bb9e9f8ae6e64612a863740e39954b9a = L.marker(
                [33.67518, -84.02458],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_9172344bdb4544d6ba6bd1df56df65c8 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_bb9e9f8ae6e64612a863740e39954b9a.setIcon(icon_9172344bdb4544d6ba6bd1df56df65c8);
        
    
        var popup_a06d572b70f14929b22f399fb784db2f = L.popup({"maxWidth": "100%"});

        
            var html_e6e8fff573be41e6a924b6c52cc75532 = $(`<div id="html_e6e8fff573be41e6a924b6c52cc75532" style="width: 100.0%; height: 100.0%;">Rating:5.0</div>`)[0];
            popup_a06d572b70f14929b22f399fb784db2f.setContent(html_e6e8fff573be41e6a924b6c52cc75532);
        

        marker_bb9e9f8ae6e64612a863740e39954b9a.bindPopup(popup_a06d572b70f14929b22f399fb784db2f)
        ;

        
    
    
            marker_bb9e9f8ae6e64612a863740e39954b9a.bindTooltip(
                `<div>
                     Gyros To-Go
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_9ee3236384074d2f8ed4ac827006c3bc = L.marker(
                [34.0011992543378, -84.08199776738971],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_8853cc1f9ed84ac4b2a8f06a71c60ef6 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_9ee3236384074d2f8ed4ac827006c3bc.setIcon(icon_8853cc1f9ed84ac4b2a8f06a71c60ef6);
        
    
        var popup_bc84d00abeb14c56b584794d2360d637 = L.popup({"maxWidth": "100%"});

        
            var html_73ed290ad3804df1ad54a30c0155956b = $(`<div id="html_73ed290ad3804df1ad54a30c0155956b" style="width: 100.0%; height: 100.0%;">Rating:5.0</div>`)[0];
            popup_bc84d00abeb14c56b584794d2360d637.setContent(html_73ed290ad3804df1ad54a30c0155956b);
        

        marker_9ee3236384074d2f8ed4ac827006c3bc.bindPopup(popup_bc84d00abeb14c56b584794d2360d637)
        ;

        
    
    
            marker_9ee3236384074d2f8ed4ac827006c3bc.bindTooltip(
                `<div>
                     Alebrije Mexican Cuisine
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_04cccbd9745a4da5a1f40e6831264879 = L.marker(
                [33.963676, -84.127119],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_08c8a658faca41d3967af6accbf8cf0c = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_04cccbd9745a4da5a1f40e6831264879.setIcon(icon_08c8a658faca41d3967af6accbf8cf0c);
        
    
        var popup_37ec92ce4fff448daf607ec799ce8478 = L.popup({"maxWidth": "100%"});

        
            var html_aec4738561f44bd1885c432a3c8d1aaa = $(`<div id="html_aec4738561f44bd1885c432a3c8d1aaa" style="width: 100.0%; height: 100.0%;">Rating:5.0</div>`)[0];
            popup_37ec92ce4fff448daf607ec799ce8478.setContent(html_aec4738561f44bd1885c432a3c8d1aaa);
        

        marker_04cccbd9745a4da5a1f40e6831264879.bindPopup(popup_37ec92ce4fff448daf607ec799ce8478)
        ;

        
    
    
            marker_04cccbd9745a4da5a1f40e6831264879.bindTooltip(
                `<div>
                     RW's Subs
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_eadb80d950894453b72e9cdd8798de66 = L.marker(
                [33.919661, -84.350803],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_724af2f779f5416ea949ba2765f1b487 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_eadb80d950894453b72e9cdd8798de66.setIcon(icon_724af2f779f5416ea949ba2765f1b487);
        
    
        var popup_a23323094add4d3295491e83c9777b95 = L.popup({"maxWidth": "100%"});

        
            var html_86fcbe6b25984bb189a4d15981e19b12 = $(`<div id="html_86fcbe6b25984bb189a4d15981e19b12" style="width: 100.0%; height: 100.0%;">Rating:5.0</div>`)[0];
            popup_a23323094add4d3295491e83c9777b95.setContent(html_86fcbe6b25984bb189a4d15981e19b12);
        

        marker_eadb80d950894453b72e9cdd8798de66.bindPopup(popup_a23323094add4d3295491e83c9777b95)
        ;

        
    
    
            marker_eadb80d950894453b72e9cdd8798de66.bindTooltip(
                `<div>
                     Local Expedition Wood Fired Grill
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_a544c1aed57546df8f515ebbe16ea157 = L.marker(
                [33.998567, -84.068797],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_f3f2b307ad0949f6b34e992c1d91d8a2 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_a544c1aed57546df8f515ebbe16ea157.setIcon(icon_f3f2b307ad0949f6b34e992c1d91d8a2);
        
    
        var popup_99f6d226e32b48ec827613076e096ce2 = L.popup({"maxWidth": "100%"});

        
            var html_7d56c7560aea436a846304832cf320ec = $(`<div id="html_7d56c7560aea436a846304832cf320ec" style="width: 100.0%; height: 100.0%;">Rating:5.0</div>`)[0];
            popup_99f6d226e32b48ec827613076e096ce2.setContent(html_7d56c7560aea436a846304832cf320ec);
        

        marker_a544c1aed57546df8f515ebbe16ea157.bindPopup(popup_99f6d226e32b48ec827613076e096ce2)
        ;

        
    
    
            marker_a544c1aed57546df8f515ebbe16ea157.bindTooltip(
                `<div>
                     Wow Poke & Juice
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_ab1822db5235466497bd2e8476e5703d = L.marker(
                [33.7408966692525, -84.3465438601188],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_61aca08e45e44447a3864fec0ee7fb4d = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_ab1822db5235466497bd2e8476e5703d.setIcon(icon_61aca08e45e44447a3864fec0ee7fb4d);
        
    
        var popup_38ca63b13007455da76acb75bd540045 = L.popup({"maxWidth": "100%"});

        
            var html_ea374b1f36ce4063b20d8d99b109bf60 = $(`<div id="html_ea374b1f36ce4063b20d8d99b109bf60" style="width: 100.0%; height: 100.0%;">Rating:5.0</div>`)[0];
            popup_38ca63b13007455da76acb75bd540045.setContent(html_ea374b1f36ce4063b20d8d99b109bf60);
        

        marker_ab1822db5235466497bd2e8476e5703d.bindPopup(popup_38ca63b13007455da76acb75bd540045)
        ;

        
    
    
            marker_ab1822db5235466497bd2e8476e5703d.bindTooltip(
                `<div>
                     Mushi Ni
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_1154eedd0d0f4941afe4bc3a4ffa15c4 = L.marker(
                [33.740908000000005, -84.34645400000001],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_e38957ac874d4112acd3b5fa429cb12a = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_1154eedd0d0f4941afe4bc3a4ffa15c4.setIcon(icon_e38957ac874d4112acd3b5fa429cb12a);
        
    
        var popup_71055c2918dc49b6ba158e97ff431294 = L.popup({"maxWidth": "100%"});

        
            var html_9371cf846b4346f2a98127cfc49271a3 = $(`<div id="html_9371cf846b4346f2a98127cfc49271a3" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_71055c2918dc49b6ba158e97ff431294.setContent(html_9371cf846b4346f2a98127cfc49271a3);
        

        marker_1154eedd0d0f4941afe4bc3a4ffa15c4.bindPopup(popup_71055c2918dc49b6ba158e97ff431294)
        ;

        
    
    
            marker_1154eedd0d0f4941afe4bc3a4ffa15c4.bindTooltip(
                `<div>
                     Poke Burri
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_623ffc64bf50405ea71558cf45d1daa7 = L.marker(
                [33.885339, -84.515763],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_0f708ad9ef5c46698bce30edfd78b857 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_623ffc64bf50405ea71558cf45d1daa7.setIcon(icon_0f708ad9ef5c46698bce30edfd78b857);
        
    
        var popup_9980f228094743588b3ca2c777910314 = L.popup({"maxWidth": "100%"});

        
            var html_5aca9941632040c9bc6e353392e25482 = $(`<div id="html_5aca9941632040c9bc6e353392e25482" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_9980f228094743588b3ca2c777910314.setContent(html_5aca9941632040c9bc6e353392e25482);
        

        marker_623ffc64bf50405ea71558cf45d1daa7.bindPopup(popup_9980f228094743588b3ca2c777910314)
        ;

        
    
    
            marker_623ffc64bf50405ea71558cf45d1daa7.bindTooltip(
                `<div>
                     Porch Light Latin Kitchen
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_de4ae301e1e042a6b646bb5a3b679e8b = L.marker(
                [34.00158, -84.08227],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_4503eb7b754e4d379b64511934eee495 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_de4ae301e1e042a6b646bb5a3b679e8b.setIcon(icon_4503eb7b754e4d379b64511934eee495);
        
    
        var popup_6373434f40b34d72becfa951887e6e84 = L.popup({"maxWidth": "100%"});

        
            var html_72cfef84634949429da96cf49707109f = $(`<div id="html_72cfef84634949429da96cf49707109f" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_6373434f40b34d72becfa951887e6e84.setContent(html_72cfef84634949429da96cf49707109f);
        

        marker_de4ae301e1e042a6b646bb5a3b679e8b.bindPopup(popup_6373434f40b34d72becfa951887e6e84)
        ;

        
    
    
            marker_de4ae301e1e042a6b646bb5a3b679e8b.bindTooltip(
                `<div>
                     KITCHEN 121
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_77b5a01999d9473faca72fde2834de0c = L.marker(
                [33.961193, -83.973016],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_7092de526e0e47d4926d1619e776e8d2 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_77b5a01999d9473faca72fde2834de0c.setIcon(icon_7092de526e0e47d4926d1619e776e8d2);
        
    
        var popup_040252345e9d4bbc9b9ab06402ac9241 = L.popup({"maxWidth": "100%"});

        
            var html_400351f7fc8b46c3859a9005eafb7a5b = $(`<div id="html_400351f7fc8b46c3859a9005eafb7a5b" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_040252345e9d4bbc9b9ab06402ac9241.setContent(html_400351f7fc8b46c3859a9005eafb7a5b);
        

        marker_77b5a01999d9473faca72fde2834de0c.bindPopup(popup_040252345e9d4bbc9b9ab06402ac9241)
        ;

        
    
    
            marker_77b5a01999d9473faca72fde2834de0c.bindTooltip(
                `<div>
                     Baozi Asian Street Food
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_6923540a64fc4c7693ba9d445cd978e0 = L.marker(
                [33.960685729980504, -84.1321487426758],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_045ebb9b50484ef8ad7620aace13eb0a = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_6923540a64fc4c7693ba9d445cd978e0.setIcon(icon_045ebb9b50484ef8ad7620aace13eb0a);
        
    
        var popup_a3d34ffa8f3d4cdda1607b38c6e65675 = L.popup({"maxWidth": "100%"});

        
            var html_93da1966158342a488e838501987e601 = $(`<div id="html_93da1966158342a488e838501987e601" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_a3d34ffa8f3d4cdda1607b38c6e65675.setContent(html_93da1966158342a488e838501987e601);
        

        marker_6923540a64fc4c7693ba9d445cd978e0.bindPopup(popup_a3d34ffa8f3d4cdda1607b38c6e65675)
        ;

        
    
    
            marker_6923540a64fc4c7693ba9d445cd978e0.bindTooltip(
                `<div>
                     Georgia French Bakery & Cafe
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_975ba2197c2c4082a2ff3e68719bdad6 = L.marker(
                [33.899071560946105, -84.20677832142641],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_31abcaa34d48414ea16b5cabd4d79027 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_975ba2197c2c4082a2ff3e68719bdad6.setIcon(icon_31abcaa34d48414ea16b5cabd4d79027);
        
    
        var popup_1cbdf5f722814d90bc71fb1217745578 = L.popup({"maxWidth": "100%"});

        
            var html_ce02c2ff0c034ef192cb4b612c6e5cf7 = $(`<div id="html_ce02c2ff0c034ef192cb4b612c6e5cf7" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_1cbdf5f722814d90bc71fb1217745578.setContent(html_ce02c2ff0c034ef192cb4b612c6e5cf7);
        

        marker_975ba2197c2c4082a2ff3e68719bdad6.bindPopup(popup_1cbdf5f722814d90bc71fb1217745578)
        ;

        
    
    
            marker_975ba2197c2c4082a2ff3e68719bdad6.bindTooltip(
                `<div>
                     Siamese Basil Thai Restaurant
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_6d1a37a802c34018865ff33d910b2972 = L.marker(
                [34.096540000000005, -84.01524],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_816aae28142c491f830a22dbe7e97c4c = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_6d1a37a802c34018865ff33d910b2972.setIcon(icon_816aae28142c491f830a22dbe7e97c4c);
        
    
        var popup_409523551dda47c7a4f1a521588c4007 = L.popup({"maxWidth": "100%"});

        
            var html_5903c2d39dee4cbbb3629b252c0dd751 = $(`<div id="html_5903c2d39dee4cbbb3629b252c0dd751" style="width: 100.0%; height: 100.0%;">Rating:5.0</div>`)[0];
            popup_409523551dda47c7a4f1a521588c4007.setContent(html_5903c2d39dee4cbbb3629b252c0dd751);
        

        marker_6d1a37a802c34018865ff33d910b2972.bindPopup(popup_409523551dda47c7a4f1a521588c4007)
        ;

        
    
    
            marker_6d1a37a802c34018865ff33d910b2972.bindTooltip(
                `<div>
                     Sugar Hill Subs
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_b5e8bf1f15a5430d9e3377d500536071 = L.marker(
                [33.8061978685091, -84.31078691035509],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_a086577d6ac7458195e2d2773664de7b = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_b5e8bf1f15a5430d9e3377d500536071.setIcon(icon_a086577d6ac7458195e2d2773664de7b);
        
    
        var popup_8e44ce7b0d56463a9112ec5e947ffb4a = L.popup({"maxWidth": "100%"});

        
            var html_b09fa7cf2db7497da832b6c4898032b3 = $(`<div id="html_b09fa7cf2db7497da832b6c4898032b3" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_8e44ce7b0d56463a9112ec5e947ffb4a.setContent(html_b09fa7cf2db7497da832b6c4898032b3);
        

        marker_b5e8bf1f15a5430d9e3377d500536071.bindPopup(popup_8e44ce7b0d56463a9112ec5e947ffb4a)
        ;

        
    
    
            marker_b5e8bf1f15a5430d9e3377d500536071.bindTooltip(
                `<div>
                     Golden Drops Café
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_006620ef26a84971a39b7f6fe683386f = L.marker(
                [33.961168, -84.14405],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_cbf80eb2fff743fe91722842236a49f8 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_006620ef26a84971a39b7f6fe683386f.setIcon(icon_cbf80eb2fff743fe91722842236a49f8);
        
    
        var popup_e6e7646ab78f44a1a42646b50eb54f90 = L.popup({"maxWidth": "100%"});

        
            var html_5532586c16c94519b46ebbc0c708f827 = $(`<div id="html_5532586c16c94519b46ebbc0c708f827" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_e6e7646ab78f44a1a42646b50eb54f90.setContent(html_5532586c16c94519b46ebbc0c708f827);
        

        marker_006620ef26a84971a39b7f6fe683386f.bindPopup(popup_e6e7646ab78f44a1a42646b50eb54f90)
        ;

        
    
    
            marker_006620ef26a84971a39b7f6fe683386f.bindTooltip(
                `<div>
                     VeGreen Vegetarian Fusion Restaurant
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_1f3beeabb0674cc998d476aba87fe73a = L.marker(
                [33.91993, -84.35280999999999],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_47f998f120494311a58cd968259cbbe3 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_1f3beeabb0674cc998d476aba87fe73a.setIcon(icon_47f998f120494311a58cd968259cbbe3);
        
    
        var popup_e42da45e1d3f49ce966acaf22d7bf6e9 = L.popup({"maxWidth": "100%"});

        
            var html_f05fd82d4a2b4b4f87e2bd1eeafffed9 = $(`<div id="html_f05fd82d4a2b4b4f87e2bd1eeafffed9" style="width: 100.0%; height: 100.0%;">Rating:5.0</div>`)[0];
            popup_e42da45e1d3f49ce966acaf22d7bf6e9.setContent(html_f05fd82d4a2b4b4f87e2bd1eeafffed9);
        

        marker_1f3beeabb0674cc998d476aba87fe73a.bindPopup(popup_e42da45e1d3f49ce966acaf22d7bf6e9)
        ;

        
    
    
            marker_1f3beeabb0674cc998d476aba87fe73a.bindTooltip(
                `<div>
                     Buon Fornello
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_8d066ce590454f119351497367fdaec3 = L.marker(
                [33.47801, -84.59524],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_5a57f5cb89d246cab3b376c87d1a3c87 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_8d066ce590454f119351497367fdaec3.setIcon(icon_5a57f5cb89d246cab3b376c87d1a3c87);
        
    
        var popup_1ea4f25dbbbf48d79f2912a170c6cb01 = L.popup({"maxWidth": "100%"});

        
            var html_fe5f019374ae4dd4a8af0df465313e07 = $(`<div id="html_fe5f019374ae4dd4a8af0df465313e07" style="width: 100.0%; height: 100.0%;">Rating:5.0</div>`)[0];
            popup_1ea4f25dbbbf48d79f2912a170c6cb01.setContent(html_fe5f019374ae4dd4a8af0df465313e07);
        

        marker_8d066ce590454f119351497367fdaec3.bindPopup(popup_1ea4f25dbbbf48d79f2912a170c6cb01)
        ;

        
    
    
            marker_8d066ce590454f119351497367fdaec3.bindTooltip(
                `<div>
                     She Craft Co
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_7f06f169c62f4402ab753eb54a2acbaa = L.marker(
                [33.8378954488708, -84.3103913493464],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_f0829b5fabc14c069794a08bc30ae3f0 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_7f06f169c62f4402ab753eb54a2acbaa.setIcon(icon_f0829b5fabc14c069794a08bc30ae3f0);
        
    
        var popup_d795e9cc40984ddeb8c2061bd5a73b37 = L.popup({"maxWidth": "100%"});

        
            var html_a3671938935f448c9a53e08b4a9e82ea = $(`<div id="html_a3671938935f448c9a53e08b4a9e82ea" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_d795e9cc40984ddeb8c2061bd5a73b37.setContent(html_a3671938935f448c9a53e08b4a9e82ea);
        

        marker_7f06f169c62f4402ab753eb54a2acbaa.bindPopup(popup_d795e9cc40984ddeb8c2061bd5a73b37)
        ;

        
    
    
            marker_7f06f169c62f4402ab753eb54a2acbaa.bindTooltip(
                `<div>
                     Desta Ethiopian Kitchen
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_a921515096414d0b880e74c2888b0a56 = L.marker(
                [33.7649, -84.39546],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_f0cd7cf312fb4375915698caf25f7f72 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_a921515096414d0b880e74c2888b0a56.setIcon(icon_f0cd7cf312fb4375915698caf25f7f72);
        
    
        var popup_14d14af334874322b7407bb9b32027a3 = L.popup({"maxWidth": "100%"});

        
            var html_c9542f40cfb44377b9b328b074dfce2f = $(`<div id="html_c9542f40cfb44377b9b328b074dfce2f" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_14d14af334874322b7407bb9b32027a3.setContent(html_c9542f40cfb44377b9b328b074dfce2f);
        

        marker_a921515096414d0b880e74c2888b0a56.bindPopup(popup_14d14af334874322b7407bb9b32027a3)
        ;

        
    
    
            marker_a921515096414d0b880e74c2888b0a56.bindTooltip(
                `<div>
                     Atlanta Breakfast Club
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_94085bf8335940abb5686e68b04296eb = L.marker(
                [33.95255, -84.57267],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_339c9aa23c9a421bb4325a3a19c1daba = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_94085bf8335940abb5686e68b04296eb.setIcon(icon_339c9aa23c9a421bb4325a3a19c1daba);
        
    
        var popup_9cbc064b8f2841f1b405b8c29deb8be6 = L.popup({"maxWidth": "100%"});

        
            var html_d203f772cbf8434798ad22ab9fc52f04 = $(`<div id="html_d203f772cbf8434798ad22ab9fc52f04" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_9cbc064b8f2841f1b405b8c29deb8be6.setContent(html_d203f772cbf8434798ad22ab9fc52f04);
        

        marker_94085bf8335940abb5686e68b04296eb.bindPopup(popup_9cbc064b8f2841f1b405b8c29deb8be6)
        ;

        
    
    
            marker_94085bf8335940abb5686e68b04296eb.bindTooltip(
                `<div>
                     Hoboken Cafe on Whitlock
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_5fb22cef8d4442fe83792b6e7f52ed23 = L.marker(
                [33.78025, -84.41095],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_6d40aabbbc784618a4db385f0da334d4 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_5fb22cef8d4442fe83792b6e7f52ed23.setIcon(icon_6d40aabbbc784618a4db385f0da334d4);
        
    
        var popup_0df5d6a93cc6426aa163b1907e91af73 = L.popup({"maxWidth": "100%"});

        
            var html_4b0f92dd38db4997b25173e13b766ac3 = $(`<div id="html_4b0f92dd38db4997b25173e13b766ac3" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_0df5d6a93cc6426aa163b1907e91af73.setContent(html_4b0f92dd38db4997b25173e13b766ac3);
        

        marker_5fb22cef8d4442fe83792b6e7f52ed23.bindPopup(popup_0df5d6a93cc6426aa163b1907e91af73)
        ;

        
    
    
            marker_5fb22cef8d4442fe83792b6e7f52ed23.bindTooltip(
                `<div>
                     Eight Sushi Lounge
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_2944448e47114b018e28a5e48ab82759 = L.marker(
                [33.445430789957, -84.1348483300247],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_0ef1697fc30142129d5bc1da8f300fb5 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_2944448e47114b018e28a5e48ab82759.setIcon(icon_0ef1697fc30142129d5bc1da8f300fb5);
        
    
        var popup_87b83a690d7c4251849a29f26e12a96a = L.popup({"maxWidth": "100%"});

        
            var html_c2472158dde3479c95438d6599a3ec0e = $(`<div id="html_c2472158dde3479c95438d6599a3ec0e" style="width: 100.0%; height: 100.0%;">Rating:5.0</div>`)[0];
            popup_87b83a690d7c4251849a29f26e12a96a.setContent(html_c2472158dde3479c95438d6599a3ec0e);
        

        marker_2944448e47114b018e28a5e48ab82759.bindPopup(popup_87b83a690d7c4251849a29f26e12a96a)
        ;

        
    
    
            marker_2944448e47114b018e28a5e48ab82759.bindTooltip(
                `<div>
                     BoJaynes
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_ee93875d96f24a909492603abaa98d47 = L.marker(
                [33.792737, -84.30502829999999],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_0f349006259b4e269c53ef525e6afd72 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_ee93875d96f24a909492603abaa98d47.setIcon(icon_0f349006259b4e269c53ef525e6afd72);
        
    
        var popup_1d705455b3f6473391b2b5f9fb5dcb48 = L.popup({"maxWidth": "100%"});

        
            var html_8d2361ab5d174035ae338724f125dd32 = $(`<div id="html_8d2361ab5d174035ae338724f125dd32" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_1d705455b3f6473391b2b5f9fb5dcb48.setContent(html_8d2361ab5d174035ae338724f125dd32);
        

        marker_ee93875d96f24a909492603abaa98d47.bindPopup(popup_1d705455b3f6473391b2b5f9fb5dcb48)
        ;

        
    
    
            marker_ee93875d96f24a909492603abaa98d47.bindTooltip(
                `<div>
                     The Po'Boy Shop
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_453c91545c94400584c67e9884676a4e = L.marker(
                [33.889179999999996, -84.382094],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_8653241a91eb40dbaf0fe50e10318795 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_453c91545c94400584c67e9884676a4e.setIcon(icon_8653241a91eb40dbaf0fe50e10318795);
        
    
        var popup_9c08ed9d1aa442078ec23a64e048e731 = L.popup({"maxWidth": "100%"});

        
            var html_044e4a76ea24441bb6757a6d951814e8 = $(`<div id="html_044e4a76ea24441bb6757a6d951814e8" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_9c08ed9d1aa442078ec23a64e048e731.setContent(html_044e4a76ea24441bb6757a6d951814e8);
        

        marker_453c91545c94400584c67e9884676a4e.bindPopup(popup_9c08ed9d1aa442078ec23a64e048e731)
        ;

        
    
    
            marker_453c91545c94400584c67e9884676a4e.bindTooltip(
                `<div>
                     Cupanion’s Kitchen & Coffee
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_1127f8df2f064cbe8249b266f0034ade = L.marker(
                [33.86823, -84.29985],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_240fb3f7bfae416299f992fac7a9f870 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_1127f8df2f064cbe8249b266f0034ade.setIcon(icon_240fb3f7bfae416299f992fac7a9f870);
        
    
        var popup_2b7820ebcaa9477393eb7b4324772257 = L.popup({"maxWidth": "100%"});

        
            var html_99854938a3264657a17d1e8c5898797f = $(`<div id="html_99854938a3264657a17d1e8c5898797f" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_2b7820ebcaa9477393eb7b4324772257.setContent(html_99854938a3264657a17d1e8c5898797f);
        

        marker_1127f8df2f064cbe8249b266f0034ade.bindPopup(popup_2b7820ebcaa9477393eb7b4324772257)
        ;

        
    
    
            marker_1127f8df2f064cbe8249b266f0034ade.bindTooltip(
                `<div>
                     Deshi Street Bangladeshi Restaurant
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_855ef3984d374d72b17b267915736d93 = L.marker(
                [33.8908506450845, -84.2853294293409],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_f15b165103a7401aa2e1eba5df4fcd2b = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_855ef3984d374d72b17b267915736d93.setIcon(icon_f15b165103a7401aa2e1eba5df4fcd2b);
        
    
        var popup_ff4ff25671be42aea610fbd3ff56f7c2 = L.popup({"maxWidth": "100%"});

        
            var html_f798f0bdf26e48e48a08385dd68d038f = $(`<div id="html_f798f0bdf26e48e48a08385dd68d038f" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_ff4ff25671be42aea610fbd3ff56f7c2.setContent(html_f798f0bdf26e48e48a08385dd68d038f);
        

        marker_855ef3984d374d72b17b267915736d93.bindPopup(popup_ff4ff25671be42aea610fbd3ff56f7c2)
        ;

        
    
    
            marker_855ef3984d374d72b17b267915736d93.bindTooltip(
                `<div>
                     Hi Pot Doraville
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_43f0491ea2ed4443b6068386a8a0d65f = L.marker(
                [34.0302686, -84.3615449],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_1e8e7057bff64f86821ad43e1b485950 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_43f0491ea2ed4443b6068386a8a0d65f.setIcon(icon_1e8e7057bff64f86821ad43e1b485950);
        
    
        var popup_6a808f13fe4943f390f688ebf0030bf0 = L.popup({"maxWidth": "100%"});

        
            var html_b47df955eb2d424e8c267fd1f26b2abb = $(`<div id="html_b47df955eb2d424e8c267fd1f26b2abb" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_6a808f13fe4943f390f688ebf0030bf0.setContent(html_b47df955eb2d424e8c267fd1f26b2abb);
        

        marker_43f0491ea2ed4443b6068386a8a0d65f.bindPopup(popup_6a808f13fe4943f390f688ebf0030bf0)
        ;

        
    
    
            marker_43f0491ea2ed4443b6068386a8a0d65f.bindTooltip(
                `<div>
                     Gracious Plenty Bakery & Breakfast
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_051b6be718454e30b2b1cc98f97a5daa = L.marker(
                [33.438834705155, -84.588817871624],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_dddb55a1ffee43989dd759333102785b = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_051b6be718454e30b2b1cc98f97a5daa.setIcon(icon_dddb55a1ffee43989dd759333102785b);
        
    
        var popup_fd5d6180ccb148eab0fb89aa914d3067 = L.popup({"maxWidth": "100%"});

        
            var html_6e6e1bbc3d97450cb664d8cbfbc5fb41 = $(`<div id="html_6e6e1bbc3d97450cb664d8cbfbc5fb41" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_fd5d6180ccb148eab0fb89aa914d3067.setContent(html_6e6e1bbc3d97450cb664d8cbfbc5fb41);
        

        marker_051b6be718454e30b2b1cc98f97a5daa.bindPopup(popup_fd5d6180ccb148eab0fb89aa914d3067)
        ;

        
    
    
            marker_051b6be718454e30b2b1cc98f97a5daa.bindTooltip(
                `<div>
                     The Beirut
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_f8f0500750374ca1b070bac8500e7a91 = L.marker(
                [34.086292, -84.518799],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_30d9d897123c4af8bff58c19928675fd = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_f8f0500750374ca1b070bac8500e7a91.setIcon(icon_30d9d897123c4af8bff58c19928675fd);
        
    
        var popup_4b1fc87e4ab74146980839d2e77f1169 = L.popup({"maxWidth": "100%"});

        
            var html_31a762f358a5410ebb3b3bc691aa117a = $(`<div id="html_31a762f358a5410ebb3b3bc691aa117a" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_4b1fc87e4ab74146980839d2e77f1169.setContent(html_31a762f358a5410ebb3b3bc691aa117a);
        

        marker_f8f0500750374ca1b070bac8500e7a91.bindPopup(popup_4b1fc87e4ab74146980839d2e77f1169)
        ;

        
    
    
            marker_f8f0500750374ca1b070bac8500e7a91.bindTooltip(
                `<div>
                     Cylantros Woodstock
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_90a5c04c2d724ce99756da96fb93c731 = L.marker(
                [34.068121000000005, -83.98105600000001],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_dddd4a2abe3241f1a86fa105ab4bb6aa = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_90a5c04c2d724ce99756da96fb93c731.setIcon(icon_dddd4a2abe3241f1a86fa105ab4bb6aa);
        
    
        var popup_61da3344c27b454594305867b04f9202 = L.popup({"maxWidth": "100%"});

        
            var html_02d6da17465e409abdff4f8b5c17ffcf = $(`<div id="html_02d6da17465e409abdff4f8b5c17ffcf" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_61da3344c27b454594305867b04f9202.setContent(html_02d6da17465e409abdff4f8b5c17ffcf);
        

        marker_90a5c04c2d724ce99756da96fb93c731.bindPopup(popup_61da3344c27b454594305867b04f9202)
        ;

        
    
    
            marker_90a5c04c2d724ce99756da96fb93c731.bindTooltip(
                `<div>
                     Wicked sushi & grill
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_1324a17b0b2c49eabcb9f5cc9768771c = L.marker(
                [33.9831999, -84.17089],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_394a74e04bf240699a788ac8c8a8e655 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_1324a17b0b2c49eabcb9f5cc9768771c.setIcon(icon_394a74e04bf240699a788ac8c8a8e655);
        
    
        var popup_cd5acc21704e436b8424a3e011ca3a2f = L.popup({"maxWidth": "100%"});

        
            var html_2716426f7abb456a9d936f112e948a28 = $(`<div id="html_2716426f7abb456a9d936f112e948a28" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_cd5acc21704e436b8424a3e011ca3a2f.setContent(html_2716426f7abb456a9d936f112e948a28);
        

        marker_1324a17b0b2c49eabcb9f5cc9768771c.bindPopup(popup_cd5acc21704e436b8424a3e011ca3a2f)
        ;

        
    
    
            marker_1324a17b0b2c49eabcb9f5cc9768771c.bindTooltip(
                `<div>
                     Rice n' Pie
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_544343b5519e44488de3e1c868e411a0 = L.marker(
                [33.758312, -84.390376],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_4c82fc5021044fc58c77f6baf7878031 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_544343b5519e44488de3e1c868e411a0.setIcon(icon_4c82fc5021044fc58c77f6baf7878031);
        
    
        var popup_6ff778048acf469f8ab94949c2d23893 = L.popup({"maxWidth": "100%"});

        
            var html_8071f0cdedf045eda83d3fe76a012105 = $(`<div id="html_8071f0cdedf045eda83d3fe76a012105" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_6ff778048acf469f8ab94949c2d23893.setContent(html_8071f0cdedf045eda83d3fe76a012105);
        

        marker_544343b5519e44488de3e1c868e411a0.bindPopup(popup_6ff778048acf469f8ab94949c2d23893)
        ;

        
    
    
            marker_544343b5519e44488de3e1c868e411a0.bindTooltip(
                `<div>
                     The Food Shoppe
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_94ee05cab2954fae9f31d2f1d8d8e783 = L.marker(
                [33.877123, -84.293591],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_d267a69cc530472e9a9e9a25b0d123a6 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_94ee05cab2954fae9f31d2f1d8d8e783.setIcon(icon_d267a69cc530472e9a9e9a25b0d123a6);
        
    
        var popup_6ba8160a251b4df1ad3dc2c2f8a3b0ee = L.popup({"maxWidth": "100%"});

        
            var html_c57f0322d252447ca4b512e9f15349fc = $(`<div id="html_c57f0322d252447ca4b512e9f15349fc" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_6ba8160a251b4df1ad3dc2c2f8a3b0ee.setContent(html_c57f0322d252447ca4b512e9f15349fc);
        

        marker_94ee05cab2954fae9f31d2f1d8d8e783.bindPopup(popup_6ba8160a251b4df1ad3dc2c2f8a3b0ee)
        ;

        
    
    
            marker_94ee05cab2954fae9f31d2f1d8d8e783.bindTooltip(
                `<div>
                     Purnima Bangladeshi Cuisine
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_dee5bfc4a18a4300b12f53bee06634f1 = L.marker(
                [34.06528, -84.21079],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_3e7e1b880a644b398174da6d6b785cc5 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_dee5bfc4a18a4300b12f53bee06634f1.setIcon(icon_3e7e1b880a644b398174da6d6b785cc5);
        
    
        var popup_a90eb58d85e54e928028dbf2b1cdad5b = L.popup({"maxWidth": "100%"});

        
            var html_b868b07b59d7490080c82240436fe51b = $(`<div id="html_b868b07b59d7490080c82240436fe51b" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_a90eb58d85e54e928028dbf2b1cdad5b.setContent(html_b868b07b59d7490080c82240436fe51b);
        

        marker_dee5bfc4a18a4300b12f53bee06634f1.bindPopup(popup_a90eb58d85e54e928028dbf2b1cdad5b)
        ;

        
    
    
            marker_dee5bfc4a18a4300b12f53bee06634f1.bindTooltip(
                `<div>
                     Hen Mother Cookhouse
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_cd347866615d40e8bf897bb4c36bf809 = L.marker(
                [33.712097799999995, -84.1060287],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_0619e90a82a7429ca461cf5342c599d0 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_cd347866615d40e8bf897bb4c36bf809.setIcon(icon_0619e90a82a7429ca461cf5342c599d0);
        
    
        var popup_64b3d20787fb41a494b36689c3f64138 = L.popup({"maxWidth": "100%"});

        
            var html_b327830711e147c6adb90366cccb817e = $(`<div id="html_b327830711e147c6adb90366cccb817e" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_64b3d20787fb41a494b36689c3f64138.setContent(html_b327830711e147c6adb90366cccb817e);
        

        marker_cd347866615d40e8bf897bb4c36bf809.bindPopup(popup_64b3d20787fb41a494b36689c3f64138)
        ;

        
    
    
            marker_cd347866615d40e8bf897bb4c36bf809.bindTooltip(
                `<div>
                     Green Love Kitchen
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_3a05a69b6e334a9da9e525ca98a4896c = L.marker(
                [33.6592449, -84.4342218],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_38453307be9b4808a17e419ab60aa8bd = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_3a05a69b6e334a9da9e525ca98a4896c.setIcon(icon_38453307be9b4808a17e419ab60aa8bd);
        
    
        var popup_587752e59c684e13827efb5c2849e5d9 = L.popup({"maxWidth": "100%"});

        
            var html_a2cde7ae87754621847ac15a1a2d0ed2 = $(`<div id="html_a2cde7ae87754621847ac15a1a2d0ed2" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_587752e59c684e13827efb5c2849e5d9.setContent(html_a2cde7ae87754621847ac15a1a2d0ed2);
        

        marker_3a05a69b6e334a9da9e525ca98a4896c.bindPopup(popup_587752e59c684e13827efb5c2849e5d9)
        ;

        
    
    
            marker_3a05a69b6e334a9da9e525ca98a4896c.bindTooltip(
                `<div>
                     Louisiana Bistreaux - East Point
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_17fcfffdc4f84d3f871aecd0491570b3 = L.marker(
                [33.7684, -84.38226],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_51d5f777a5a845acbac5e052fcb4cd41 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_17fcfffdc4f84d3f871aecd0491570b3.setIcon(icon_51d5f777a5a845acbac5e052fcb4cd41);
        
    
        var popup_e676e51d447a4e61bf1d49cda0ff490f = L.popup({"maxWidth": "100%"});

        
            var html_b55e5aefc38c4d46baf5caa450971f13 = $(`<div id="html_b55e5aefc38c4d46baf5caa450971f13" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_e676e51d447a4e61bf1d49cda0ff490f.setContent(html_b55e5aefc38c4d46baf5caa450971f13);
        

        marker_17fcfffdc4f84d3f871aecd0491570b3.bindPopup(popup_e676e51d447a4e61bf1d49cda0ff490f)
        ;

        
    
    
            marker_17fcfffdc4f84d3f871aecd0491570b3.bindTooltip(
                `<div>
                     Poor Calvin's
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_07935ed20f7d4280a438952f6a644e88 = L.marker(
                [33.83534, -84.33755],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_f30c089ac0e740529c981d7d6f33cf45 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_07935ed20f7d4280a438952f6a644e88.setIcon(icon_f30c089ac0e740529c981d7d6f33cf45);
        
    
        var popup_7aebbd3cbe3742f7a8a152e157d106e5 = L.popup({"maxWidth": "100%"});

        
            var html_bf53eb7324964a1b93fe24d0b2296819 = $(`<div id="html_bf53eb7324964a1b93fe24d0b2296819" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_7aebbd3cbe3742f7a8a152e157d106e5.setContent(html_bf53eb7324964a1b93fe24d0b2296819);
        

        marker_07935ed20f7d4280a438952f6a644e88.bindPopup(popup_7aebbd3cbe3742f7a8a152e157d106e5)
        ;

        
    
    
            marker_07935ed20f7d4280a438952f6a644e88.bindTooltip(
                `<div>
                     Roc South Cuisine
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_fba64885d83b410faad137ce603fab56 = L.marker(
                [34.0704462896031, -84.207593412828],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_5233c21de6ea4a1f91a29acb746ed890 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_fba64885d83b410faad137ce603fab56.setIcon(icon_5233c21de6ea4a1f91a29acb746ed890);
        
    
        var popup_b5218481aacc47bfb36c46101ffb4e82 = L.popup({"maxWidth": "100%"});

        
            var html_ff03b8e5813c4f4b8611f8d4bc940db8 = $(`<div id="html_ff03b8e5813c4f4b8611f8d4bc940db8" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_b5218481aacc47bfb36c46101ffb4e82.setContent(html_ff03b8e5813c4f4b8611f8d4bc940db8);
        

        marker_fba64885d83b410faad137ce603fab56.bindPopup(popup_b5218481aacc47bfb36c46101ffb4e82)
        ;

        
    
    
            marker_fba64885d83b410faad137ce603fab56.bindTooltip(
                `<div>
                     El Trompo Mexican Taqueria
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_4e1cb9c796074080880b0fe27870bfdf = L.marker(
                [33.8127799, -84.35473],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_fa4294ef4b5d42139af05e724d7f3fc6 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_4e1cb9c796074080880b0fe27870bfdf.setIcon(icon_fa4294ef4b5d42139af05e724d7f3fc6);
        
    
        var popup_e1396d8181804cd4b30e93a32a0e8538 = L.popup({"maxWidth": "100%"});

        
            var html_e7184f15157f49649a74d35835b98bb9 = $(`<div id="html_e7184f15157f49649a74d35835b98bb9" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_e1396d8181804cd4b30e93a32a0e8538.setContent(html_e7184f15157f49649a74d35835b98bb9);
        

        marker_4e1cb9c796074080880b0fe27870bfdf.bindPopup(popup_e1396d8181804cd4b30e93a32a0e8538)
        ;

        
    
    
            marker_4e1cb9c796074080880b0fe27870bfdf.bindTooltip(
                `<div>
                     Embilta Café & Restaurant Ethiopian Cuisine
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_f2024f47c1724aa68c0975d0f3e04fac = L.marker(
                [34.08712, -84.47279],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_8733274dc2e0489eb0a84d3ec70e0677 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_f2024f47c1724aa68c0975d0f3e04fac.setIcon(icon_8733274dc2e0489eb0a84d3ec70e0677);
        
    
        var popup_a6c095220a34426c9d7da3d52b0bc679 = L.popup({"maxWidth": "100%"});

        
            var html_485729eadd8e40aabd3b827a873b3856 = $(`<div id="html_485729eadd8e40aabd3b827a873b3856" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_a6c095220a34426c9d7da3d52b0bc679.setContent(html_485729eadd8e40aabd3b827a873b3856);
        

        marker_f2024f47c1724aa68c0975d0f3e04fac.bindPopup(popup_a6c095220a34426c9d7da3d52b0bc679)
        ;

        
    
    
            marker_f2024f47c1724aa68c0975d0f3e04fac.bindTooltip(
                `<div>
                     The Sahara Grill
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_91452a7c1e124509a1345c1b39260b23 = L.marker(
                [34.0008872704639, -84.5883881952453],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_eb64cfabf801449a9579fdf25e29a33c = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_91452a7c1e124509a1345c1b39260b23.setIcon(icon_eb64cfabf801449a9579fdf25e29a33c);
        
    
        var popup_f2e8519c425143c1aa515ad3a275e99b = L.popup({"maxWidth": "100%"});

        
            var html_7a1df934dc014acba275e4a8e35a07ab = $(`<div id="html_7a1df934dc014acba275e4a8e35a07ab" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_f2e8519c425143c1aa515ad3a275e99b.setContent(html_7a1df934dc014acba275e4a8e35a07ab);
        

        marker_91452a7c1e124509a1345c1b39260b23.bindPopup(popup_f2e8519c425143c1aa515ad3a275e99b)
        ;

        
    
    
            marker_91452a7c1e124509a1345c1b39260b23.bindTooltip(
                `<div>
                     Taj Mahal Grill
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_fc36080f5f7c480b856648b3f701aaa0 = L.marker(
                [33.8566085797099, -84.38271659804009],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_614c296435014eb3b1062dabb5d8df74 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_fc36080f5f7c480b856648b3f701aaa0.setIcon(icon_614c296435014eb3b1062dabb5d8df74);
        
    
        var popup_12f31053d2cb4a72ae797eb61cd0f895 = L.popup({"maxWidth": "100%"});

        
            var html_41fbd3235d4c4c2e8137de062a5c0407 = $(`<div id="html_41fbd3235d4c4c2e8137de062a5c0407" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_12f31053d2cb4a72ae797eb61cd0f895.setContent(html_41fbd3235d4c4c2e8137de062a5c0407);
        

        marker_fc36080f5f7c480b856648b3f701aaa0.bindPopup(popup_12f31053d2cb4a72ae797eb61cd0f895)
        ;

        
    
    
            marker_fc36080f5f7c480b856648b3f701aaa0.bindTooltip(
                `<div>
                     JINYA Ramen Bar
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_523d8ba9bbf142288465dc941ed8a1e6 = L.marker(
                [33.9475624005883, -84.33496600000001],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_1e792e638f634463b12447bfcfca381a = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_523d8ba9bbf142288465dc941ed8a1e6.setIcon(icon_1e792e638f634463b12447bfcfca381a);
        
    
        var popup_7d7c2a365cf64f0d9331b424327aa213 = L.popup({"maxWidth": "100%"});

        
            var html_9a2144c5f97546b88e7763b91e3efb28 = $(`<div id="html_9a2144c5f97546b88e7763b91e3efb28" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_7d7c2a365cf64f0d9331b424327aa213.setContent(html_9a2144c5f97546b88e7763b91e3efb28);
        

        marker_523d8ba9bbf142288465dc941ed8a1e6.bindPopup(popup_7d7c2a365cf64f0d9331b424327aa213)
        ;

        
    
    
            marker_523d8ba9bbf142288465dc941ed8a1e6.bindTooltip(
                `<div>
                     NFA Burger
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_240bc239f04c46e18f4f1ffbbf9f1ff4 = L.marker(
                [34.107667, -84.552378],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_6b58a3a20f164c5086d9e760fe9fbc8c = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_240bc239f04c46e18f4f1ffbbf9f1ff4.setIcon(icon_6b58a3a20f164c5086d9e760fe9fbc8c);
        
    
        var popup_9c5bd205ba6d44729b87bcbfa884451c = L.popup({"maxWidth": "100%"});

        
            var html_e88db8bee7fb4527ab9d4406b24e2303 = $(`<div id="html_e88db8bee7fb4527ab9d4406b24e2303" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_9c5bd205ba6d44729b87bcbfa884451c.setContent(html_e88db8bee7fb4527ab9d4406b24e2303);
        

        marker_240bc239f04c46e18f4f1ffbbf9f1ff4.bindPopup(popup_9c5bd205ba6d44729b87bcbfa884451c)
        ;

        
    
    
            marker_240bc239f04c46e18f4f1ffbbf9f1ff4.bindTooltip(
                `<div>
                     Kpop Bbq and Bar
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_e7b7b4c271474cf7bfafcdd056451302 = L.marker(
                [33.8986473470416, -84.44717852760309],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_5550d4ae29a341129b8781669ff6b4c0 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_e7b7b4c271474cf7bfafcdd056451302.setIcon(icon_5550d4ae29a341129b8781669ff6b4c0);
        
    
        var popup_c01934682bea410694b321b66f51ba0a = L.popup({"maxWidth": "100%"});

        
            var html_df0cba8d373042e28ee7238cfe518b72 = $(`<div id="html_df0cba8d373042e28ee7238cfe518b72" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_c01934682bea410694b321b66f51ba0a.setContent(html_df0cba8d373042e28ee7238cfe518b72);
        

        marker_e7b7b4c271474cf7bfafcdd056451302.bindPopup(popup_c01934682bea410694b321b66f51ba0a)
        ;

        
    
    
            marker_e7b7b4c271474cf7bfafcdd056451302.bindTooltip(
                `<div>
                     Heirloom Market BBQ
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_0b7f047169e741ca9e75b93a363fd2dd = L.marker(
                [33.9411734961952, -84.2125377030411],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_282af50f3c66461f844c353bed259899 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_0b7f047169e741ca9e75b93a363fd2dd.setIcon(icon_282af50f3c66461f844c353bed259899);
        
    
        var popup_4d5cddbd4df14b2aa30f1efbdd9cb227 = L.popup({"maxWidth": "100%"});

        
            var html_353c29e6831a49919b4a16e43eb20305 = $(`<div id="html_353c29e6831a49919b4a16e43eb20305" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_4d5cddbd4df14b2aa30f1efbdd9cb227.setContent(html_353c29e6831a49919b4a16e43eb20305);
        

        marker_0b7f047169e741ca9e75b93a363fd2dd.bindPopup(popup_4d5cddbd4df14b2aa30f1efbdd9cb227)
        ;

        
    
    
            marker_0b7f047169e741ca9e75b93a363fd2dd.bindTooltip(
                `<div>
                     Bleu House
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_585b81e6291a4d20a36576b7abdabfb4 = L.marker(
                [34.0403326, -84.34251529999999],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_3c4fd744283f4e66a7f773c83e71e74e = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_585b81e6291a4d20a36576b7abdabfb4.setIcon(icon_3c4fd744283f4e66a7f773c83e71e74e);
        
    
        var popup_d5228c5551624e74927058b563d475f8 = L.popup({"maxWidth": "100%"});

        
            var html_ff15800d779243048ac08401d3a3c22a = $(`<div id="html_ff15800d779243048ac08401d3a3c22a" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_d5228c5551624e74927058b563d475f8.setContent(html_ff15800d779243048ac08401d3a3c22a);
        

        marker_585b81e6291a4d20a36576b7abdabfb4.bindPopup(popup_d5228c5551624e74927058b563d475f8)
        ;

        
    
    
            marker_585b81e6291a4d20a36576b7abdabfb4.bindTooltip(
                `<div>
                     Jerusalem Chef Restaurant
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_dfe31206428e45edaebbbafdcf883d46 = L.marker(
                [33.9520084, -84.5488322],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_778e7129be684bdc9ed8a27dfebf1d6b = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_dfe31206428e45edaebbbafdcf883d46.setIcon(icon_778e7129be684bdc9ed8a27dfebf1d6b);
        
    
        var popup_2576a103ed074650955dd8081fc451b2 = L.popup({"maxWidth": "100%"});

        
            var html_d8a21937e8fb4d1eb2dd74eac2d0ff71 = $(`<div id="html_d8a21937e8fb4d1eb2dd74eac2d0ff71" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_2576a103ed074650955dd8081fc451b2.setContent(html_d8a21937e8fb4d1eb2dd74eac2d0ff71);
        

        marker_dfe31206428e45edaebbbafdcf883d46.bindPopup(popup_2576a103ed074650955dd8081fc451b2)
        ;

        
    
    
            marker_dfe31206428e45edaebbbafdcf883d46.bindTooltip(
                `<div>
                     The Marietta Local
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_09c5fd41111946118ee99ee9fa7879c6 = L.marker(
                [34.0178225891952, -84.6195390075445],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_39f8988363be45d89266c930998924fc = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_09c5fd41111946118ee99ee9fa7879c6.setIcon(icon_39f8988363be45d89266c930998924fc);
        
    
        var popup_a703b41e5c7541d08c41b7079318463f = L.popup({"maxWidth": "100%"});

        
            var html_3607077f0ad94010b936e246128030c0 = $(`<div id="html_3607077f0ad94010b936e246128030c0" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_a703b41e5c7541d08c41b7079318463f.setContent(html_3607077f0ad94010b936e246128030c0);
        

        marker_09c5fd41111946118ee99ee9fa7879c6.bindPopup(popup_a703b41e5c7541d08c41b7079318463f)
        ;

        
    
    
            marker_09c5fd41111946118ee99ee9fa7879c6.bindTooltip(
                `<div>
                     Italia Mediterranean Grill
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_6108da4917964f089a1bb48022774e7a = L.marker(
                [33.8929143, -84.47794329999999],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_2c9bde13b924447e995a781ea7f0bf1c = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_6108da4917964f089a1bb48022774e7a.setIcon(icon_2c9bde13b924447e995a781ea7f0bf1c);
        
    
        var popup_e0833da0cf8447af9d708bfbd79cd37c = L.popup({"maxWidth": "100%"});

        
            var html_3435c7ede3ca42728fe4cb52020f1784 = $(`<div id="html_3435c7ede3ca42728fe4cb52020f1784" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_e0833da0cf8447af9d708bfbd79cd37c.setContent(html_3435c7ede3ca42728fe4cb52020f1784);
        

        marker_6108da4917964f089a1bb48022774e7a.bindPopup(popup_e0833da0cf8447af9d708bfbd79cd37c)
        ;

        
    
    
            marker_6108da4917964f089a1bb48022774e7a.bindTooltip(
                `<div>
                     Tacos La Villa
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_31354e1adc1140de86158264e43af8a0 = L.marker(
                [34.02839, -84.65044],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_83b2632f1a5f472895991000c4b19943 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_31354e1adc1140de86158264e43af8a0.setIcon(icon_83b2632f1a5f472895991000c4b19943);
        
    
        var popup_4d0c6427665b47c7b8e24675e9ede918 = L.popup({"maxWidth": "100%"});

        
            var html_f29d2aec26f14b89b17bc2522b6e232a = $(`<div id="html_f29d2aec26f14b89b17bc2522b6e232a" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_4d0c6427665b47c7b8e24675e9ede918.setContent(html_f29d2aec26f14b89b17bc2522b6e232a);
        

        marker_31354e1adc1140de86158264e43af8a0.bindPopup(popup_4d0c6427665b47c7b8e24675e9ede918)
        ;

        
    
    
            marker_31354e1adc1140de86158264e43af8a0.bindTooltip(
                `<div>
                     Pita King
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_78d2ef9931a94be2ac75304fc1683d12 = L.marker(
                [33.867515000000004, -84.19169699999999],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_b3aa6da1c58e4d88a62b5a82a4c91fd7 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_78d2ef9931a94be2ac75304fc1683d12.setIcon(icon_b3aa6da1c58e4d88a62b5a82a4c91fd7);
        
    
        var popup_e586b83f635a475da9a743f98c15accb = L.popup({"maxWidth": "100%"});

        
            var html_ba128442d0e84e0cb91cc7a82166ec6b = $(`<div id="html_ba128442d0e84e0cb91cc7a82166ec6b" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_e586b83f635a475da9a743f98c15accb.setContent(html_ba128442d0e84e0cb91cc7a82166ec6b);
        

        marker_78d2ef9931a94be2ac75304fc1683d12.bindPopup(popup_e586b83f635a475da9a743f98c15accb)
        ;

        
    
    
            marker_78d2ef9931a94be2ac75304fc1683d12.bindTooltip(
                `<div>
                     Taqueria San Pancho
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_76e3141521ca43528825e101caed8657 = L.marker(
                [34.0188297326194, -84.3117081666565],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_5f7fd531df174bbc9189eaf1d90ff8ad = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_76e3141521ca43528825e101caed8657.setIcon(icon_5f7fd531df174bbc9189eaf1d90ff8ad);
        
    
        var popup_2a649c9f75d74635886bb14f554e2887 = L.popup({"maxWidth": "100%"});

        
            var html_ab80da73411d4b5f863c4ef5fa7a10ef = $(`<div id="html_ab80da73411d4b5f863c4ef5fa7a10ef" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_2a649c9f75d74635886bb14f554e2887.setContent(html_ab80da73411d4b5f863c4ef5fa7a10ef);
        

        marker_76e3141521ca43528825e101caed8657.bindPopup(popup_2a649c9f75d74635886bb14f554e2887)
        ;

        
    
    
            marker_76e3141521ca43528825e101caed8657.bindTooltip(
                `<div>
                     Foundation Social Eatery
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_3512161750d04e038d60d1a9664ae033 = L.marker(
                [34.0136946869881, -84.5675291148193],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_f5621eeb1d17439d9d1e69ca5f066d17 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_3512161750d04e038d60d1a9664ae033.setIcon(icon_f5621eeb1d17439d9d1e69ca5f066d17);
        
    
        var popup_da9550a626cb439cbfd56b37f8b2d247 = L.popup({"maxWidth": "100%"});

        
            var html_503015c245c74d34b9cc81824780c289 = $(`<div id="html_503015c245c74d34b9cc81824780c289" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_da9550a626cb439cbfd56b37f8b2d247.setContent(html_503015c245c74d34b9cc81824780c289);
        

        marker_3512161750d04e038d60d1a9664ae033.bindPopup(popup_da9550a626cb439cbfd56b37f8b2d247)
        ;

        
    
    
            marker_3512161750d04e038d60d1a9664ae033.bindTooltip(
                `<div>
                     The Rotisserie Shop
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_7cba39c2e7f241bf9c24793e97522294 = L.marker(
                [34.0167198820803, -84.362401664257],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_0e4e47ea65274f3bba066bacad1621c7 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_7cba39c2e7f241bf9c24793e97522294.setIcon(icon_0e4e47ea65274f3bba066bacad1621c7);
        
    
        var popup_eb0d28889596420aa4af7a8e62920cd8 = L.popup({"maxWidth": "100%"});

        
            var html_e91d51873cc542c1a914a0caed12af6c = $(`<div id="html_e91d51873cc542c1a914a0caed12af6c" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_eb0d28889596420aa4af7a8e62920cd8.setContent(html_e91d51873cc542c1a914a0caed12af6c);
        

        marker_7cba39c2e7f241bf9c24793e97522294.bindPopup(popup_eb0d28889596420aa4af7a8e62920cd8)
        ;

        
    
    
            marker_7cba39c2e7f241bf9c24793e97522294.bindTooltip(
                `<div>
                     Chippers Pub
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_6368daacfb8947fd93a56cfea2c73bb7 = L.marker(
                [33.882797, -84.50488299999999],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_a40e3b675055427185d0ab1704595e68 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_6368daacfb8947fd93a56cfea2c73bb7.setIcon(icon_a40e3b675055427185d0ab1704595e68);
        
    
        var popup_69a0536fe953457cbc7f6ad0147012dd = L.popup({"maxWidth": "100%"});

        
            var html_137e75a9220a4fa3a9c0da50ef415ffe = $(`<div id="html_137e75a9220a4fa3a9c0da50ef415ffe" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_69a0536fe953457cbc7f6ad0147012dd.setContent(html_137e75a9220a4fa3a9c0da50ef415ffe);
        

        marker_6368daacfb8947fd93a56cfea2c73bb7.bindPopup(popup_69a0536fe953457cbc7f6ad0147012dd)
        ;

        
    
    
            marker_6368daacfb8947fd93a56cfea2c73bb7.bindTooltip(
                `<div>
                     Mezza Luna
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_ffe5c5ae22cd464fad50a04ade0d93aa = L.marker(
                [33.8075938694564, -84.3935011499407],
                {"color": "green"}
            ).addTo(marker_cluster_7285d904a9fd4e188799aa89de9be8c0);
        
    
            var icon_447a043a2767479f836676791eddfacd = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "utensils", "iconColor": "white", "markerColor": "blue", "prefix": "fa"}
            );
            marker_ffe5c5ae22cd464fad50a04ade0d93aa.setIcon(icon_447a043a2767479f836676791eddfacd);
        
    
        var popup_acd4f708ccd748a38e97a60429ac465c = L.popup({"maxWidth": "100%"});

        
            var html_202f59cd79f2430ebc692c375104c42f = $(`<div id="html_202f59cd79f2430ebc692c375104c42f" style="width: 100.0%; height: 100.0%;">Rating:4.5</div>`)[0];
            popup_acd4f708ccd748a38e97a60429ac465c.setContent(html_202f59cd79f2430ebc692c375104c42f);
        

        marker_ffe5c5ae22cd464fad50a04ade0d93aa.bindPopup(popup_acd4f708ccd748a38e97a60429ac465c)
        ;

        
    
    
            marker_ffe5c5ae22cd464fad50a04ade0d93aa.bindTooltip(
                `<div>
                     gusto!
                 </div>`,
                {"sticky": true}
            );
        
</script>
