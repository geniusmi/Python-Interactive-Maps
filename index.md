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
                #map_4e26dc9626a9455d95e73248c091f5b5 {
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
    
            <div class="folium-map" id="map_4e26dc9626a9455d95e73248c091f5b5" ></div>
        
</body>
<script>    
    
            var map_4e26dc9626a9455d95e73248c091f5b5 = L.map(
                "map_4e26dc9626a9455d95e73248c091f5b5",
                {
                    center: [33.75, -84.33],
                    crs: L.CRS.EPSG3857,
                    zoom: 12,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );

            

        
    
            var tile_layer_de133bdbb05c41c1a053776671e7680d = L.tileLayer(
                "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                {"attribution": "Data by \u0026copy; \u003ca href=\"http://openstreetmap.org\"\u003eOpenStreetMap\u003c/a\u003e, under \u003ca href=\"http://www.openstreetmap.org/copyright\"\u003eODbL\u003c/a\u003e.", "detectRetina": false, "maxNativeZoom": 18, "maxZoom": 18, "minZoom": 0, "noWrap": false, "opacity": 1, "subdomains": "abc", "tms": false}
            ).addTo(map_4e26dc9626a9455d95e73248c091f5b5);
        
    
            var marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f = L.markerClusterGroup(
                {}
            );
            map_4e26dc9626a9455d95e73248c091f5b5.addLayer(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var marker_8c688f10195e4f9cb538abf040ab8636 = L.marker(
                [33.760538145529196, -84.38655546480409],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_25b9dc557cbb4878b74eed7078c88b22 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_8c688f10195e4f9cb538abf040ab8636.setIcon(icon_25b9dc557cbb4878b74eed7078c88b22);
        
    
        var popup_15cb791fc38447c9a814664f1f5691de = L.popup({"maxWidth": "100%"});

        
            var html_9f453ebb4eb64c9ab961f0ac2e54e2ef = $(`<div id="html_9f453ebb4eb64c9ab961f0ac2e54e2ef" style="width: 100.0%; height: 100.0%;">Aviva by Kameel</div>`)[0];
            popup_15cb791fc38447c9a814664f1f5691de.setContent(html_9f453ebb4eb64c9ab961f0ac2e54e2ef);
        

        marker_8c688f10195e4f9cb538abf040ab8636.bindPopup(popup_15cb791fc38447c9a814664f1f5691de)
        ;

        
    
    
            var marker_559e13ec2976423ab836e02192a1383c = L.marker(
                [34.089366, -84.27497840000001],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_aa597085567944608065049bf4299d77 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_559e13ec2976423ab836e02192a1383c.setIcon(icon_aa597085567944608065049bf4299d77);
        
    
        var popup_10508f19bd514fca87d4db2835768038 = L.popup({"maxWidth": "100%"});

        
            var html_87f704f77227404c89a347dd34b9acc0 = $(`<div id="html_87f704f77227404c89a347dd34b9acc0" style="width: 100.0%; height: 100.0%;">Local Expedition Wood Fired Grill</div>`)[0];
            popup_10508f19bd514fca87d4db2835768038.setContent(html_87f704f77227404c89a347dd34b9acc0);
        

        marker_559e13ec2976423ab836e02192a1383c.bindPopup(popup_10508f19bd514fca87d4db2835768038)
        ;

        
    
    
            var marker_42260555031c48438b35d84d5c3ca6cb = L.marker(
                [34.005762, -84.603604],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_7f717cfc63294f3fb8d821ea635fd255 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_42260555031c48438b35d84d5c3ca6cb.setIcon(icon_7f717cfc63294f3fb8d821ea635fd255);
        
    
        var popup_85632ef0fd1544549ddb173f1f5c3627 = L.popup({"maxWidth": "100%"});

        
            var html_73e9605a80da4c209577b93aa6a229b7 = $(`<div id="html_73e9605a80da4c209577b93aa6a229b7" style="width: 100.0%; height: 100.0%;">Tacos Del Chavo</div>`)[0];
            popup_85632ef0fd1544549ddb173f1f5c3627.setContent(html_73e9605a80da4c209577b93aa6a229b7);
        

        marker_42260555031c48438b35d84d5c3ca6cb.bindPopup(popup_85632ef0fd1544549ddb173f1f5c3627)
        ;

        
    
    
            var marker_81a62b16b2074bb1a0f899429a76708b = L.marker(
                [33.74075, -84.34672990000001],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_2b2f7bc9901c4542b92e160f5e7033c6 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_81a62b16b2074bb1a0f899429a76708b.setIcon(icon_2b2f7bc9901c4542b92e160f5e7033c6);
        
    
        var popup_59816ca200444d29a97cb515e77688de = L.popup({"maxWidth": "100%"});

        
            var html_e7d910e233854ca0907c846a7115f578 = $(`<div id="html_e7d910e233854ca0907c846a7115f578" style="width: 100.0%; height: 100.0%;">Marrakech Express</div>`)[0];
            popup_59816ca200444d29a97cb515e77688de.setContent(html_e7d910e233854ca0907c846a7115f578);
        

        marker_81a62b16b2074bb1a0f899429a76708b.bindPopup(popup_59816ca200444d29a97cb515e77688de)
        ;

        
    
    
            var marker_c1f3dd261beb436a97e04ca26909fdee = L.marker(
                [34.0753984, -84.29597640000001],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_b0f6961cc47f4c2daca469f007fd4c04 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_c1f3dd261beb436a97e04ca26909fdee.setIcon(icon_b0f6961cc47f4c2daca469f007fd4c04);
        
    
        var popup_ca1cf6de5f08433cae142ec976f9da2b = L.popup({"maxWidth": "100%"});

        
            var html_a2ab6ac20e6a4b4ea1ecd7adda4da176 = $(`<div id="html_a2ab6ac20e6a4b4ea1ecd7adda4da176" style="width: 100.0%; height: 100.0%;">Valor Coffee</div>`)[0];
            popup_ca1cf6de5f08433cae142ec976f9da2b.setContent(html_a2ab6ac20e6a4b4ea1ecd7adda4da176);
        

        marker_c1f3dd261beb436a97e04ca26909fdee.bindPopup(popup_ca1cf6de5f08433cae142ec976f9da2b)
        ;

        
    
    
            var marker_c005351a5be64cdf86ebb954ec1cd098 = L.marker(
                [33.891135, -84.504663],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_65387082906749329d6a511b316ffff3 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_c005351a5be64cdf86ebb954ec1cd098.setIcon(icon_65387082906749329d6a511b316ffff3);
        
    
        var popup_1eb97b9e987d41f7baaca2339db916fa = L.popup({"maxWidth": "100%"});

        
            var html_9e48c1cde8c7421bb9669736601c85d3 = $(`<div id="html_9e48c1cde8c7421bb9669736601c85d3" style="width: 100.0%; height: 100.0%;">Himalayan Kitchen</div>`)[0];
            popup_1eb97b9e987d41f7baaca2339db916fa.setContent(html_9e48c1cde8c7421bb9669736601c85d3);
        

        marker_c005351a5be64cdf86ebb954ec1cd098.bindPopup(popup_1eb97b9e987d41f7baaca2339db916fa)
        ;

        
    
    
            var marker_80764265c4114909a490e74cc2954470 = L.marker(
                [33.67518, -84.02458],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_faa98b42fe4945228971258c6ed6e8bd = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_80764265c4114909a490e74cc2954470.setIcon(icon_faa98b42fe4945228971258c6ed6e8bd);
        
    
        var popup_e645cb47ba4448a9b15a45b3734b3703 = L.popup({"maxWidth": "100%"});

        
            var html_cba43444054f42fea44b779c80ed41fc = $(`<div id="html_cba43444054f42fea44b779c80ed41fc" style="width: 100.0%; height: 100.0%;">Gyros To-Go</div>`)[0];
            popup_e645cb47ba4448a9b15a45b3734b3703.setContent(html_cba43444054f42fea44b779c80ed41fc);
        

        marker_80764265c4114909a490e74cc2954470.bindPopup(popup_e645cb47ba4448a9b15a45b3734b3703)
        ;

        
    
    
            var marker_a58fb2da80994cc4a6a8ad38caff58bb = L.marker(
                [34.0011992543378, -84.08199776738971],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_50e2805d94054638884601ef162e91dc = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_a58fb2da80994cc4a6a8ad38caff58bb.setIcon(icon_50e2805d94054638884601ef162e91dc);
        
    
        var popup_3001c3fb01934212b7a6436924547482 = L.popup({"maxWidth": "100%"});

        
            var html_96c9c14e69eb4e20b08b0285fa2a64ec = $(`<div id="html_96c9c14e69eb4e20b08b0285fa2a64ec" style="width: 100.0%; height: 100.0%;">Alebrije Mexican Cuisine</div>`)[0];
            popup_3001c3fb01934212b7a6436924547482.setContent(html_96c9c14e69eb4e20b08b0285fa2a64ec);
        

        marker_a58fb2da80994cc4a6a8ad38caff58bb.bindPopup(popup_3001c3fb01934212b7a6436924547482)
        ;

        
    
    
            var marker_7c75d936499b40048ea6d2c2d23313e8 = L.marker(
                [33.963676, -84.127119],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_784ee9dc8b224d18be0699c77eec1aa3 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_7c75d936499b40048ea6d2c2d23313e8.setIcon(icon_784ee9dc8b224d18be0699c77eec1aa3);
        
    
        var popup_995d517d78ce4008a68b7962af89d409 = L.popup({"maxWidth": "100%"});

        
            var html_3f1f0de4887743c2bdf604e4e55152e4 = $(`<div id="html_3f1f0de4887743c2bdf604e4e55152e4" style="width: 100.0%; height: 100.0%;">RW's Subs</div>`)[0];
            popup_995d517d78ce4008a68b7962af89d409.setContent(html_3f1f0de4887743c2bdf604e4e55152e4);
        

        marker_7c75d936499b40048ea6d2c2d23313e8.bindPopup(popup_995d517d78ce4008a68b7962af89d409)
        ;

        
    
    
            var marker_958dcb4827f14d1fa98c858628a348d5 = L.marker(
                [33.919661, -84.350803],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_137376bc4b0047bea2d3794ad9d90b70 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_958dcb4827f14d1fa98c858628a348d5.setIcon(icon_137376bc4b0047bea2d3794ad9d90b70);
        
    
        var popup_7ebd5c996ee04d3d8874059aa5561946 = L.popup({"maxWidth": "100%"});

        
            var html_21d9493dfce044e5956647c96dfc2225 = $(`<div id="html_21d9493dfce044e5956647c96dfc2225" style="width: 100.0%; height: 100.0%;">Local Expedition Wood Fired Grill</div>`)[0];
            popup_7ebd5c996ee04d3d8874059aa5561946.setContent(html_21d9493dfce044e5956647c96dfc2225);
        

        marker_958dcb4827f14d1fa98c858628a348d5.bindPopup(popup_7ebd5c996ee04d3d8874059aa5561946)
        ;

        
    
    
            var marker_545df3c466794ce889a7bba6b1400c4f = L.marker(
                [33.998567, -84.068797],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_c3db774d217f49e28f5d2645c2d91032 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_545df3c466794ce889a7bba6b1400c4f.setIcon(icon_c3db774d217f49e28f5d2645c2d91032);
        
    
        var popup_a8ed4cbdb7e24c88b5eba8ee956315d3 = L.popup({"maxWidth": "100%"});

        
            var html_64b222ac3ca54653acc8fe5a00835deb = $(`<div id="html_64b222ac3ca54653acc8fe5a00835deb" style="width: 100.0%; height: 100.0%;">Wow Poke & Juice</div>`)[0];
            popup_a8ed4cbdb7e24c88b5eba8ee956315d3.setContent(html_64b222ac3ca54653acc8fe5a00835deb);
        

        marker_545df3c466794ce889a7bba6b1400c4f.bindPopup(popup_a8ed4cbdb7e24c88b5eba8ee956315d3)
        ;

        
    
    
            var marker_d9c9f95e8fc5494593b56c2d002ea87b = L.marker(
                [33.7408966692525, -84.3465438601188],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_057066f320704bb7a96c0eb997bd0f23 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_d9c9f95e8fc5494593b56c2d002ea87b.setIcon(icon_057066f320704bb7a96c0eb997bd0f23);
        
    
        var popup_af74896d8e1045d5becc9f6a30210c85 = L.popup({"maxWidth": "100%"});

        
            var html_88ec930ef8704f2fb40e746218ad3ac4 = $(`<div id="html_88ec930ef8704f2fb40e746218ad3ac4" style="width: 100.0%; height: 100.0%;">Mushi Ni</div>`)[0];
            popup_af74896d8e1045d5becc9f6a30210c85.setContent(html_88ec930ef8704f2fb40e746218ad3ac4);
        

        marker_d9c9f95e8fc5494593b56c2d002ea87b.bindPopup(popup_af74896d8e1045d5becc9f6a30210c85)
        ;

        
    
    
            var marker_d8886e58caf44969bc5ad9965a459c0f = L.marker(
                [33.740908000000005, -84.34645400000001],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_e93a17566f204539a7154841b297f803 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_d8886e58caf44969bc5ad9965a459c0f.setIcon(icon_e93a17566f204539a7154841b297f803);
        
    
        var popup_43c372aa78ca47dd99824e28187546cb = L.popup({"maxWidth": "100%"});

        
            var html_cf1a826975d14c489c5eb65e05743bc3 = $(`<div id="html_cf1a826975d14c489c5eb65e05743bc3" style="width: 100.0%; height: 100.0%;">Poke Burri</div>`)[0];
            popup_43c372aa78ca47dd99824e28187546cb.setContent(html_cf1a826975d14c489c5eb65e05743bc3);
        

        marker_d8886e58caf44969bc5ad9965a459c0f.bindPopup(popup_43c372aa78ca47dd99824e28187546cb)
        ;

        
    
    
            var marker_2dc4e72075da4620bf33c5980b9ee7c2 = L.marker(
                [33.885339, -84.515763],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_4a14a9f34ab24d06927da8bd0ee861fb = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_2dc4e72075da4620bf33c5980b9ee7c2.setIcon(icon_4a14a9f34ab24d06927da8bd0ee861fb);
        
    
        var popup_3ba082ffd5244f688a73f18ef3967410 = L.popup({"maxWidth": "100%"});

        
            var html_20c0817422d348f5879037c83ece383b = $(`<div id="html_20c0817422d348f5879037c83ece383b" style="width: 100.0%; height: 100.0%;">Porch Light Latin Kitchen</div>`)[0];
            popup_3ba082ffd5244f688a73f18ef3967410.setContent(html_20c0817422d348f5879037c83ece383b);
        

        marker_2dc4e72075da4620bf33c5980b9ee7c2.bindPopup(popup_3ba082ffd5244f688a73f18ef3967410)
        ;

        
    
    
            var marker_f9c3d21a7a89478d95302c063149b9f1 = L.marker(
                [34.00158, -84.08227],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_7ab9b75b056f4bd7bdbbd6fa6340c804 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_f9c3d21a7a89478d95302c063149b9f1.setIcon(icon_7ab9b75b056f4bd7bdbbd6fa6340c804);
        
    
        var popup_5c10085956124264ab71d23d2e2b605b = L.popup({"maxWidth": "100%"});

        
            var html_7aeb97c5bc764edaa82b7e52d7458a1b = $(`<div id="html_7aeb97c5bc764edaa82b7e52d7458a1b" style="width: 100.0%; height: 100.0%;">KITCHEN 121</div>`)[0];
            popup_5c10085956124264ab71d23d2e2b605b.setContent(html_7aeb97c5bc764edaa82b7e52d7458a1b);
        

        marker_f9c3d21a7a89478d95302c063149b9f1.bindPopup(popup_5c10085956124264ab71d23d2e2b605b)
        ;

        
    
    
            var marker_17f15806799d4089a5fe9a1bab94f040 = L.marker(
                [33.961193, -83.973016],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_af3aa349655b4a7dbb7cb68465f5741a = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_17f15806799d4089a5fe9a1bab94f040.setIcon(icon_af3aa349655b4a7dbb7cb68465f5741a);
        
    
        var popup_993533f18c8e47b28b8da0073a54d134 = L.popup({"maxWidth": "100%"});

        
            var html_b9e8209e9fe74dabb255f48283aecb58 = $(`<div id="html_b9e8209e9fe74dabb255f48283aecb58" style="width: 100.0%; height: 100.0%;">Baozi Asian Street Food</div>`)[0];
            popup_993533f18c8e47b28b8da0073a54d134.setContent(html_b9e8209e9fe74dabb255f48283aecb58);
        

        marker_17f15806799d4089a5fe9a1bab94f040.bindPopup(popup_993533f18c8e47b28b8da0073a54d134)
        ;

        
    
    
            var marker_cb178544ecd64356b306f7427e4b5535 = L.marker(
                [33.960685729980504, -84.1321487426758],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_97919bebf6114420b4ff78bf0e99992b = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_cb178544ecd64356b306f7427e4b5535.setIcon(icon_97919bebf6114420b4ff78bf0e99992b);
        
    
        var popup_786ca0ffa5eb4cebaceaea9156b7d66d = L.popup({"maxWidth": "100%"});

        
            var html_9097bcf716074a569375ed2cfd3260ed = $(`<div id="html_9097bcf716074a569375ed2cfd3260ed" style="width: 100.0%; height: 100.0%;">Georgia French Bakery & Cafe</div>`)[0];
            popup_786ca0ffa5eb4cebaceaea9156b7d66d.setContent(html_9097bcf716074a569375ed2cfd3260ed);
        

        marker_cb178544ecd64356b306f7427e4b5535.bindPopup(popup_786ca0ffa5eb4cebaceaea9156b7d66d)
        ;

        
    
    
            var marker_24b08ec8910e4f30a51813892c68add2 = L.marker(
                [33.899071560946105, -84.20677832142641],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_59b3228b80eb40e6b4b91169e0d3660e = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_24b08ec8910e4f30a51813892c68add2.setIcon(icon_59b3228b80eb40e6b4b91169e0d3660e);
        
    
        var popup_7b415a4cbfc44eaf9ec02e9f46363b3f = L.popup({"maxWidth": "100%"});

        
            var html_6fb4ede6fa3c4e43a3bd97513f952683 = $(`<div id="html_6fb4ede6fa3c4e43a3bd97513f952683" style="width: 100.0%; height: 100.0%;">Siamese Basil Thai Restaurant</div>`)[0];
            popup_7b415a4cbfc44eaf9ec02e9f46363b3f.setContent(html_6fb4ede6fa3c4e43a3bd97513f952683);
        

        marker_24b08ec8910e4f30a51813892c68add2.bindPopup(popup_7b415a4cbfc44eaf9ec02e9f46363b3f)
        ;

        
    
    
            var marker_0aa0c1cc7a3e4407918578f9046a0b70 = L.marker(
                [34.096540000000005, -84.01524],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_6975ab255dbb4bbe9252baeb065f137f = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_0aa0c1cc7a3e4407918578f9046a0b70.setIcon(icon_6975ab255dbb4bbe9252baeb065f137f);
        
    
        var popup_5ee36502afe84311bae26b6d8dc53b0f = L.popup({"maxWidth": "100%"});

        
            var html_d4f931a48ad64acc97d80a2c2572f8c4 = $(`<div id="html_d4f931a48ad64acc97d80a2c2572f8c4" style="width: 100.0%; height: 100.0%;">Sugar Hill Subs</div>`)[0];
            popup_5ee36502afe84311bae26b6d8dc53b0f.setContent(html_d4f931a48ad64acc97d80a2c2572f8c4);
        

        marker_0aa0c1cc7a3e4407918578f9046a0b70.bindPopup(popup_5ee36502afe84311bae26b6d8dc53b0f)
        ;

        
    
    
            var marker_6b2015596b464641b1af4ee9f01c7a98 = L.marker(
                [34.117019653320305, -84.0098571777344],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_40b6d1aa955e49c6846f759d65b19b07 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_6b2015596b464641b1af4ee9f01c7a98.setIcon(icon_40b6d1aa955e49c6846f759d65b19b07);
        
    
        var popup_f5601fa0a30a48778889a54ed93a1cab = L.popup({"maxWidth": "100%"});

        
            var html_b642ba374ac9441da2b23deb32470f25 = $(`<div id="html_b642ba374ac9441da2b23deb32470f25" style="width: 100.0%; height: 100.0%;">Ricos World Kitchen</div>`)[0];
            popup_f5601fa0a30a48778889a54ed93a1cab.setContent(html_b642ba374ac9441da2b23deb32470f25);
        

        marker_6b2015596b464641b1af4ee9f01c7a98.bindPopup(popup_f5601fa0a30a48778889a54ed93a1cab)
        ;

        
    
    
            var marker_e3818db78153420aa3a08fbcc65dc2d9 = L.marker(
                [33.8061978685091, -84.31078691035509],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_8b1929e13db7411193a5d2e02aa66b6f = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_e3818db78153420aa3a08fbcc65dc2d9.setIcon(icon_8b1929e13db7411193a5d2e02aa66b6f);
        
    
        var popup_836fbabd38f246c690f6f9824f262897 = L.popup({"maxWidth": "100%"});

        
            var html_8e8fcd85ad4a44c38781f34ffda34b00 = $(`<div id="html_8e8fcd85ad4a44c38781f34ffda34b00" style="width: 100.0%; height: 100.0%;">Golden Drops Café</div>`)[0];
            popup_836fbabd38f246c690f6f9824f262897.setContent(html_8e8fcd85ad4a44c38781f34ffda34b00);
        

        marker_e3818db78153420aa3a08fbcc65dc2d9.bindPopup(popup_836fbabd38f246c690f6f9824f262897)
        ;

        
    
    
            var marker_61257270555c45758bd6517e3e322977 = L.marker(
                [33.961168, -84.14405],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_9eb619b01182413e94ddd824e40b1324 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_61257270555c45758bd6517e3e322977.setIcon(icon_9eb619b01182413e94ddd824e40b1324);
        
    
        var popup_cd80803d99db4805825720986b1e13ec = L.popup({"maxWidth": "100%"});

        
            var html_6bb876e5ebcc40608b1be89580766fd2 = $(`<div id="html_6bb876e5ebcc40608b1be89580766fd2" style="width: 100.0%; height: 100.0%;">VeGreen Vegetarian Fusion Restaurant</div>`)[0];
            popup_cd80803d99db4805825720986b1e13ec.setContent(html_6bb876e5ebcc40608b1be89580766fd2);
        

        marker_61257270555c45758bd6517e3e322977.bindPopup(popup_cd80803d99db4805825720986b1e13ec)
        ;

        
    
    
            var marker_d2a53307d7ea461daee379a523bf011d = L.marker(
                [33.91993, -84.35280999999999],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_094480917d2842e7a3396edc575e412a = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_d2a53307d7ea461daee379a523bf011d.setIcon(icon_094480917d2842e7a3396edc575e412a);
        
    
        var popup_0e7b8aec454f43aabbee30aff647700d = L.popup({"maxWidth": "100%"});

        
            var html_84370cf55eb345e1b745d585a0ddfea0 = $(`<div id="html_84370cf55eb345e1b745d585a0ddfea0" style="width: 100.0%; height: 100.0%;">Buon Fornello</div>`)[0];
            popup_0e7b8aec454f43aabbee30aff647700d.setContent(html_84370cf55eb345e1b745d585a0ddfea0);
        

        marker_d2a53307d7ea461daee379a523bf011d.bindPopup(popup_0e7b8aec454f43aabbee30aff647700d)
        ;

        
    
    
            var marker_c4b8e934dbd14753b71073c53dfad87c = L.marker(
                [33.47801, -84.59524],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_2a2148dee53a4a089a6bfa250fd1cc66 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_c4b8e934dbd14753b71073c53dfad87c.setIcon(icon_2a2148dee53a4a089a6bfa250fd1cc66);
        
    
        var popup_b3fbb57e836640ae9980863e7c424308 = L.popup({"maxWidth": "100%"});

        
            var html_91e69997408742469708ce264766b03f = $(`<div id="html_91e69997408742469708ce264766b03f" style="width: 100.0%; height: 100.0%;">She Craft Co</div>`)[0];
            popup_b3fbb57e836640ae9980863e7c424308.setContent(html_91e69997408742469708ce264766b03f);
        

        marker_c4b8e934dbd14753b71073c53dfad87c.bindPopup(popup_b3fbb57e836640ae9980863e7c424308)
        ;

        
    
    
            var marker_e33b53cda3f34ff3990030bb02160131 = L.marker(
                [33.8378954488708, -84.3103913493464],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_739054682f184c7cbd67360aab97d40a = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_e33b53cda3f34ff3990030bb02160131.setIcon(icon_739054682f184c7cbd67360aab97d40a);
        
    
        var popup_87ff3b8256cd4b1c950bd8395330b664 = L.popup({"maxWidth": "100%"});

        
            var html_1394d3af892147bfab89044e1dcff9b6 = $(`<div id="html_1394d3af892147bfab89044e1dcff9b6" style="width: 100.0%; height: 100.0%;">Desta Ethiopian Kitchen</div>`)[0];
            popup_87ff3b8256cd4b1c950bd8395330b664.setContent(html_1394d3af892147bfab89044e1dcff9b6);
        

        marker_e33b53cda3f34ff3990030bb02160131.bindPopup(popup_87ff3b8256cd4b1c950bd8395330b664)
        ;

        
    
    
            var marker_76c8e3d3563e43bbab86b5cff5ae35f9 = L.marker(
                [33.7649, -84.39546],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_c5669d13eb534983895a0538f6b4d5e5 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_76c8e3d3563e43bbab86b5cff5ae35f9.setIcon(icon_c5669d13eb534983895a0538f6b4d5e5);
        
    
        var popup_fa6eb522c6fb464193a83893eac45ef4 = L.popup({"maxWidth": "100%"});

        
            var html_ae13aec1baf34f1f9353688aded7ce97 = $(`<div id="html_ae13aec1baf34f1f9353688aded7ce97" style="width: 100.0%; height: 100.0%;">Atlanta Breakfast Club</div>`)[0];
            popup_fa6eb522c6fb464193a83893eac45ef4.setContent(html_ae13aec1baf34f1f9353688aded7ce97);
        

        marker_76c8e3d3563e43bbab86b5cff5ae35f9.bindPopup(popup_fa6eb522c6fb464193a83893eac45ef4)
        ;

        
    
    
            var marker_0baca872ea0e42198abd53815f564e73 = L.marker(
                [33.95255, -84.57267],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_4bd684338b9f46b9b03509d418ecc7ed = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_0baca872ea0e42198abd53815f564e73.setIcon(icon_4bd684338b9f46b9b03509d418ecc7ed);
        
    
        var popup_1da8d85c6dcc49dba7df9829a9ff356e = L.popup({"maxWidth": "100%"});

        
            var html_8b147d6e4b8f4c9487e1e2f284b3ab57 = $(`<div id="html_8b147d6e4b8f4c9487e1e2f284b3ab57" style="width: 100.0%; height: 100.0%;">Hoboken Cafe on Whitlock</div>`)[0];
            popup_1da8d85c6dcc49dba7df9829a9ff356e.setContent(html_8b147d6e4b8f4c9487e1e2f284b3ab57);
        

        marker_0baca872ea0e42198abd53815f564e73.bindPopup(popup_1da8d85c6dcc49dba7df9829a9ff356e)
        ;

        
    
    
            var marker_e3e038aa667349b9967b3b002a3cf896 = L.marker(
                [33.78025, -84.41095],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_2811a6979fb74fddafba88d3474ecb4d = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_e3e038aa667349b9967b3b002a3cf896.setIcon(icon_2811a6979fb74fddafba88d3474ecb4d);
        
    
        var popup_8f914f055acf485a81edcc43c0751592 = L.popup({"maxWidth": "100%"});

        
            var html_6401c576b1a942c19f9f7d50d44e596c = $(`<div id="html_6401c576b1a942c19f9f7d50d44e596c" style="width: 100.0%; height: 100.0%;">Eight Sushi Lounge</div>`)[0];
            popup_8f914f055acf485a81edcc43c0751592.setContent(html_6401c576b1a942c19f9f7d50d44e596c);
        

        marker_e3e038aa667349b9967b3b002a3cf896.bindPopup(popup_8f914f055acf485a81edcc43c0751592)
        ;

        
    
    
            var marker_2a9c3b531eca48268c91b986951d3b66 = L.marker(
                [33.445430789957, -84.1348483300247],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_719e63695b3447fd9d046fe1523892b4 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_2a9c3b531eca48268c91b986951d3b66.setIcon(icon_719e63695b3447fd9d046fe1523892b4);
        
    
        var popup_1cef5d4411ff4548ae152e9b3c1ad479 = L.popup({"maxWidth": "100%"});

        
            var html_b473596f1a8943ee983f38062532364e = $(`<div id="html_b473596f1a8943ee983f38062532364e" style="width: 100.0%; height: 100.0%;">BoJaynes</div>`)[0];
            popup_1cef5d4411ff4548ae152e9b3c1ad479.setContent(html_b473596f1a8943ee983f38062532364e);
        

        marker_2a9c3b531eca48268c91b986951d3b66.bindPopup(popup_1cef5d4411ff4548ae152e9b3c1ad479)
        ;

        
    
    
            var marker_8ac4ab39a8fc4c0487dd0d8f883df44f = L.marker(
                [33.792737, -84.30502829999999],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_80bc4b106bcb4008a4fbe60e7b8d2e14 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_8ac4ab39a8fc4c0487dd0d8f883df44f.setIcon(icon_80bc4b106bcb4008a4fbe60e7b8d2e14);
        
    
        var popup_9753ce56823c4b13b9b735e0335a63af = L.popup({"maxWidth": "100%"});

        
            var html_82c638554d864b1cbb6c2b40e411a4aa = $(`<div id="html_82c638554d864b1cbb6c2b40e411a4aa" style="width: 100.0%; height: 100.0%;">The Po'Boy Shop</div>`)[0];
            popup_9753ce56823c4b13b9b735e0335a63af.setContent(html_82c638554d864b1cbb6c2b40e411a4aa);
        

        marker_8ac4ab39a8fc4c0487dd0d8f883df44f.bindPopup(popup_9753ce56823c4b13b9b735e0335a63af)
        ;

        
    
    
            var marker_7806c32c728441a880b4a7503f7b0cb6 = L.marker(
                [33.889179999999996, -84.382094],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_fcdaea767d41435587474356c0361ba3 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_7806c32c728441a880b4a7503f7b0cb6.setIcon(icon_fcdaea767d41435587474356c0361ba3);
        
    
        var popup_22998811c1b143bc90ddc13a168414f8 = L.popup({"maxWidth": "100%"});

        
            var html_5987779191424d7ab0caef051e0ae701 = $(`<div id="html_5987779191424d7ab0caef051e0ae701" style="width: 100.0%; height: 100.0%;">Cupanion’s Kitchen & Coffee</div>`)[0];
            popup_22998811c1b143bc90ddc13a168414f8.setContent(html_5987779191424d7ab0caef051e0ae701);
        

        marker_7806c32c728441a880b4a7503f7b0cb6.bindPopup(popup_22998811c1b143bc90ddc13a168414f8)
        ;

        
    
    
            var marker_e04ee0fd54e24fa9b770b42bcb7a3456 = L.marker(
                [34.107667, -84.552378],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_046d03d657af470d98a802c6e9d61cce = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_e04ee0fd54e24fa9b770b42bcb7a3456.setIcon(icon_046d03d657af470d98a802c6e9d61cce);
        
    
        var popup_3ff33b36f3fe4373b96f43e0517cc196 = L.popup({"maxWidth": "100%"});

        
            var html_f3cabfb0e87047c4bfe08b6f248a95da = $(`<div id="html_f3cabfb0e87047c4bfe08b6f248a95da" style="width: 100.0%; height: 100.0%;">Kpop Bbq and Bar</div>`)[0];
            popup_3ff33b36f3fe4373b96f43e0517cc196.setContent(html_f3cabfb0e87047c4bfe08b6f248a95da);
        

        marker_e04ee0fd54e24fa9b770b42bcb7a3456.bindPopup(popup_3ff33b36f3fe4373b96f43e0517cc196)
        ;

        
    
    
            var marker_b7528676b5c943eba7a3273a0ec69217 = L.marker(
                [33.86823, -84.29985],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_06976c6bf7da415692426fa28ac0dc0f = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_b7528676b5c943eba7a3273a0ec69217.setIcon(icon_06976c6bf7da415692426fa28ac0dc0f);
        
    
        var popup_afffa99ef9ec474ba91295f2df44ff65 = L.popup({"maxWidth": "100%"});

        
            var html_8e8cecdf94614ac0a59007be09dff70b = $(`<div id="html_8e8cecdf94614ac0a59007be09dff70b" style="width: 100.0%; height: 100.0%;">Deshi Street Bangladeshi Restaurant</div>`)[0];
            popup_afffa99ef9ec474ba91295f2df44ff65.setContent(html_8e8cecdf94614ac0a59007be09dff70b);
        

        marker_b7528676b5c943eba7a3273a0ec69217.bindPopup(popup_afffa99ef9ec474ba91295f2df44ff65)
        ;

        
    
    
            var marker_e37c0417e2b5419e86ed148515e93990 = L.marker(
                [33.8908506450845, -84.2853294293409],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_2059f292acc14f939974c28733af9d91 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_e37c0417e2b5419e86ed148515e93990.setIcon(icon_2059f292acc14f939974c28733af9d91);
        
    
        var popup_14648004a0524e21ba67467a7034132d = L.popup({"maxWidth": "100%"});

        
            var html_7bfc2a27b44846f5836c9a3ae9d57248 = $(`<div id="html_7bfc2a27b44846f5836c9a3ae9d57248" style="width: 100.0%; height: 100.0%;">Hi Pot Doraville</div>`)[0];
            popup_14648004a0524e21ba67467a7034132d.setContent(html_7bfc2a27b44846f5836c9a3ae9d57248);
        

        marker_e37c0417e2b5419e86ed148515e93990.bindPopup(popup_14648004a0524e21ba67467a7034132d)
        ;

        
    
    
            var marker_d2c9a89a824b4050a48c985d601bdc0d = L.marker(
                [34.0302686, -84.3615449],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_2c4723eaaa764b0dbecc5b81790aa9fc = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_d2c9a89a824b4050a48c985d601bdc0d.setIcon(icon_2c4723eaaa764b0dbecc5b81790aa9fc);
        
    
        var popup_833774a78d2e46198ba1092ab8ddb8ad = L.popup({"maxWidth": "100%"});

        
            var html_63b87e8510fa4c38bed57305cfd06042 = $(`<div id="html_63b87e8510fa4c38bed57305cfd06042" style="width: 100.0%; height: 100.0%;">Gracious Plenty Bakery & Breakfast</div>`)[0];
            popup_833774a78d2e46198ba1092ab8ddb8ad.setContent(html_63b87e8510fa4c38bed57305cfd06042);
        

        marker_d2c9a89a824b4050a48c985d601bdc0d.bindPopup(popup_833774a78d2e46198ba1092ab8ddb8ad)
        ;

        
    
    
            var marker_76f6cdaae5e74b3086b84e6b7b1dbbd7 = L.marker(
                [33.438834705155, -84.588817871624],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_f28c9bc478244bf28bdd46a17752c70f = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_76f6cdaae5e74b3086b84e6b7b1dbbd7.setIcon(icon_f28c9bc478244bf28bdd46a17752c70f);
        
    
        var popup_6f4e7352f62b49eb9b4badcf13446f6c = L.popup({"maxWidth": "100%"});

        
            var html_9816b8e65ec548ce89879fad19479c4f = $(`<div id="html_9816b8e65ec548ce89879fad19479c4f" style="width: 100.0%; height: 100.0%;">The Beirut</div>`)[0];
            popup_6f4e7352f62b49eb9b4badcf13446f6c.setContent(html_9816b8e65ec548ce89879fad19479c4f);
        

        marker_76f6cdaae5e74b3086b84e6b7b1dbbd7.bindPopup(popup_6f4e7352f62b49eb9b4badcf13446f6c)
        ;

        
    
    
            var marker_8abc9253bf5741ae8fb646e43d47408e = L.marker(
                [34.086292, -84.518799],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_34b57f89f8644d5d9c32510d080d497e = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_8abc9253bf5741ae8fb646e43d47408e.setIcon(icon_34b57f89f8644d5d9c32510d080d497e);
        
    
        var popup_369540dd41e943a38335f7ba3acf022a = L.popup({"maxWidth": "100%"});

        
            var html_1ecee3bd2d1544178de75dafb86156c4 = $(`<div id="html_1ecee3bd2d1544178de75dafb86156c4" style="width: 100.0%; height: 100.0%;">Cylantros Woodstock</div>`)[0];
            popup_369540dd41e943a38335f7ba3acf022a.setContent(html_1ecee3bd2d1544178de75dafb86156c4);
        

        marker_8abc9253bf5741ae8fb646e43d47408e.bindPopup(popup_369540dd41e943a38335f7ba3acf022a)
        ;

        
    
    
            var marker_4eb747a95e424212bd5368a0a50b8a65 = L.marker(
                [34.068121000000005, -83.98105600000001],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_4d45499c7a1542c0854eecaa70834290 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_4eb747a95e424212bd5368a0a50b8a65.setIcon(icon_4d45499c7a1542c0854eecaa70834290);
        
    
        var popup_997caec7e8404167bab1ac4ec0fb2320 = L.popup({"maxWidth": "100%"});

        
            var html_2573b5a22173449bb6d6129533a8f088 = $(`<div id="html_2573b5a22173449bb6d6129533a8f088" style="width: 100.0%; height: 100.0%;">Wicked sushi & grill</div>`)[0];
            popup_997caec7e8404167bab1ac4ec0fb2320.setContent(html_2573b5a22173449bb6d6129533a8f088);
        

        marker_4eb747a95e424212bd5368a0a50b8a65.bindPopup(popup_997caec7e8404167bab1ac4ec0fb2320)
        ;

        
    
    
            var marker_e8e4ad8b81f24757be1b5e47dbb135f3 = L.marker(
                [33.9831999, -84.17089],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_bf9d09c11b11401d9b4afcffd9d4103d = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_e8e4ad8b81f24757be1b5e47dbb135f3.setIcon(icon_bf9d09c11b11401d9b4afcffd9d4103d);
        
    
        var popup_00ed8d3068b04d169e98e126bd1f324c = L.popup({"maxWidth": "100%"});

        
            var html_fbaecde2e82c420e9115fabf39279010 = $(`<div id="html_fbaecde2e82c420e9115fabf39279010" style="width: 100.0%; height: 100.0%;">Rice n' Pie</div>`)[0];
            popup_00ed8d3068b04d169e98e126bd1f324c.setContent(html_fbaecde2e82c420e9115fabf39279010);
        

        marker_e8e4ad8b81f24757be1b5e47dbb135f3.bindPopup(popup_00ed8d3068b04d169e98e126bd1f324c)
        ;

        
    
    
            var marker_8059e9c6364a4ec1a41e8af50f3af30c = L.marker(
                [33.758312, -84.390376],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_31675b3349534f98a2b0e6f949414df1 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_8059e9c6364a4ec1a41e8af50f3af30c.setIcon(icon_31675b3349534f98a2b0e6f949414df1);
        
    
        var popup_6dd548d9290640c0a779309edf3e0daf = L.popup({"maxWidth": "100%"});

        
            var html_946f57866e7b46c69b777fa01f492f4a = $(`<div id="html_946f57866e7b46c69b777fa01f492f4a" style="width: 100.0%; height: 100.0%;">The Food Shoppe</div>`)[0];
            popup_6dd548d9290640c0a779309edf3e0daf.setContent(html_946f57866e7b46c69b777fa01f492f4a);
        

        marker_8059e9c6364a4ec1a41e8af50f3af30c.bindPopup(popup_6dd548d9290640c0a779309edf3e0daf)
        ;

        
    
    
            var marker_2d771f2ac80546a8a35c9992e39899af = L.marker(
                [33.877123, -84.293591],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_2aa03f7bb5ee48638499ed8962bab23b = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_2d771f2ac80546a8a35c9992e39899af.setIcon(icon_2aa03f7bb5ee48638499ed8962bab23b);
        
    
        var popup_037ea1179e5d4af78fee4eff82f77b49 = L.popup({"maxWidth": "100%"});

        
            var html_ecd68e57adf5403bbc0ebdd4e97cdb34 = $(`<div id="html_ecd68e57adf5403bbc0ebdd4e97cdb34" style="width: 100.0%; height: 100.0%;">Purnima Bangladeshi Cuisine</div>`)[0];
            popup_037ea1179e5d4af78fee4eff82f77b49.setContent(html_ecd68e57adf5403bbc0ebdd4e97cdb34);
        

        marker_2d771f2ac80546a8a35c9992e39899af.bindPopup(popup_037ea1179e5d4af78fee4eff82f77b49)
        ;

        
    
    
            var marker_376f510c6bef4b7faf45f68cbf3ed9a4 = L.marker(
                [34.06528, -84.21079],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_62c9fb1f27154c7cac654b8c37ee9c6c = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_376f510c6bef4b7faf45f68cbf3ed9a4.setIcon(icon_62c9fb1f27154c7cac654b8c37ee9c6c);
        
    
        var popup_e84c5d126bd442e38fd9c048fcb3b344 = L.popup({"maxWidth": "100%"});

        
            var html_c5bea14cffca42bfac029d90e356a062 = $(`<div id="html_c5bea14cffca42bfac029d90e356a062" style="width: 100.0%; height: 100.0%;">Hen Mother Cookhouse</div>`)[0];
            popup_e84c5d126bd442e38fd9c048fcb3b344.setContent(html_c5bea14cffca42bfac029d90e356a062);
        

        marker_376f510c6bef4b7faf45f68cbf3ed9a4.bindPopup(popup_e84c5d126bd442e38fd9c048fcb3b344)
        ;

        
    
    
            var marker_501c8c6291c24f2baa56795f00d6c494 = L.marker(
                [33.712097799999995, -84.1060287],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_8daac797d806463eafba58c976e56912 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_501c8c6291c24f2baa56795f00d6c494.setIcon(icon_8daac797d806463eafba58c976e56912);
        
    
        var popup_bf3161e7f9b84920962d7ffd2fc4db5f = L.popup({"maxWidth": "100%"});

        
            var html_9ebb07d7ff89471b839f1d4c50afacce = $(`<div id="html_9ebb07d7ff89471b839f1d4c50afacce" style="width: 100.0%; height: 100.0%;">Green Love Kitchen</div>`)[0];
            popup_bf3161e7f9b84920962d7ffd2fc4db5f.setContent(html_9ebb07d7ff89471b839f1d4c50afacce);
        

        marker_501c8c6291c24f2baa56795f00d6c494.bindPopup(popup_bf3161e7f9b84920962d7ffd2fc4db5f)
        ;

        
    
    
            var marker_eb60533075da48feb10e127e52556ddf = L.marker(
                [33.6592449, -84.4342218],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_fc5610e4a9cf4882a5a0f67f960926ac = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_eb60533075da48feb10e127e52556ddf.setIcon(icon_fc5610e4a9cf4882a5a0f67f960926ac);
        
    
        var popup_f9edf46bf71046c98d52aabf92c6fd57 = L.popup({"maxWidth": "100%"});

        
            var html_a8a02e83020a4581a60a0a4bb606464c = $(`<div id="html_a8a02e83020a4581a60a0a4bb606464c" style="width: 100.0%; height: 100.0%;">Louisiana Bistreaux - East Point</div>`)[0];
            popup_f9edf46bf71046c98d52aabf92c6fd57.setContent(html_a8a02e83020a4581a60a0a4bb606464c);
        

        marker_eb60533075da48feb10e127e52556ddf.bindPopup(popup_f9edf46bf71046c98d52aabf92c6fd57)
        ;

        
    
    
            var marker_d33404d5317f49adbe62b66f9ab204de = L.marker(
                [33.7684, -84.38226],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_8291310e63844177b15c2dda42015676 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_d33404d5317f49adbe62b66f9ab204de.setIcon(icon_8291310e63844177b15c2dda42015676);
        
    
        var popup_903611fbcdc44b1aabdbb0d06ce743ec = L.popup({"maxWidth": "100%"});

        
            var html_f7181397a53641cd99ff7b456918d496 = $(`<div id="html_f7181397a53641cd99ff7b456918d496" style="width: 100.0%; height: 100.0%;">Poor Calvin's</div>`)[0];
            popup_903611fbcdc44b1aabdbb0d06ce743ec.setContent(html_f7181397a53641cd99ff7b456918d496);
        

        marker_d33404d5317f49adbe62b66f9ab204de.bindPopup(popup_903611fbcdc44b1aabdbb0d06ce743ec)
        ;

        
    
    
            var marker_deea2eb923d9467e9aef2ede1896a8a4 = L.marker(
                [33.83534, -84.33755],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_98f13f049912495db637d733b18bee5e = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_deea2eb923d9467e9aef2ede1896a8a4.setIcon(icon_98f13f049912495db637d733b18bee5e);
        
    
        var popup_928fb023d2ed417c81a6e5e29ccbab17 = L.popup({"maxWidth": "100%"});

        
            var html_f42ead849a89400ca359314dcb649b5b = $(`<div id="html_f42ead849a89400ca359314dcb649b5b" style="width: 100.0%; height: 100.0%;">Roc South Cuisine</div>`)[0];
            popup_928fb023d2ed417c81a6e5e29ccbab17.setContent(html_f42ead849a89400ca359314dcb649b5b);
        

        marker_deea2eb923d9467e9aef2ede1896a8a4.bindPopup(popup_928fb023d2ed417c81a6e5e29ccbab17)
        ;

        
    
    
            var marker_9fa7feb2e6694d118a3bda7da970da0a = L.marker(
                [34.0704462896031, -84.207593412828],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_94bb675063ea477984539f50a97109f9 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_9fa7feb2e6694d118a3bda7da970da0a.setIcon(icon_94bb675063ea477984539f50a97109f9);
        
    
        var popup_a101a70000af495582ccb6ebfeb437a9 = L.popup({"maxWidth": "100%"});

        
            var html_f560ca67db4745628634121c37028d47 = $(`<div id="html_f560ca67db4745628634121c37028d47" style="width: 100.0%; height: 100.0%;">El Trompo Mexican Taqueria</div>`)[0];
            popup_a101a70000af495582ccb6ebfeb437a9.setContent(html_f560ca67db4745628634121c37028d47);
        

        marker_9fa7feb2e6694d118a3bda7da970da0a.bindPopup(popup_a101a70000af495582ccb6ebfeb437a9)
        ;

        
    
    
            var marker_439a4568f24e4a05a05477b4d479e9bf = L.marker(
                [33.8127799, -84.35473],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_76cc47cdae7b4fe89d7cec008b557235 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_439a4568f24e4a05a05477b4d479e9bf.setIcon(icon_76cc47cdae7b4fe89d7cec008b557235);
        
    
        var popup_210a44c22d0e4f788e79435dd0b6eb5e = L.popup({"maxWidth": "100%"});

        
            var html_09c64b99be5541c8a8e1a3ff8f2754a0 = $(`<div id="html_09c64b99be5541c8a8e1a3ff8f2754a0" style="width: 100.0%; height: 100.0%;">Embilta Café & Restaurant Ethiopian Cuisine</div>`)[0];
            popup_210a44c22d0e4f788e79435dd0b6eb5e.setContent(html_09c64b99be5541c8a8e1a3ff8f2754a0);
        

        marker_439a4568f24e4a05a05477b4d479e9bf.bindPopup(popup_210a44c22d0e4f788e79435dd0b6eb5e)
        ;

        
    
    
            var marker_5cc11434e0e54457ab017b7bd5a3e490 = L.marker(
                [34.08712, -84.47279],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_fd4dd71f07fd4baaa7e2856dbf9ffee6 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_5cc11434e0e54457ab017b7bd5a3e490.setIcon(icon_fd4dd71f07fd4baaa7e2856dbf9ffee6);
        
    
        var popup_d5fb704f185548d1b96873092b2a3d71 = L.popup({"maxWidth": "100%"});

        
            var html_18a364e67e704ee59bdd3e183bb5f972 = $(`<div id="html_18a364e67e704ee59bdd3e183bb5f972" style="width: 100.0%; height: 100.0%;">The Sahara Grill</div>`)[0];
            popup_d5fb704f185548d1b96873092b2a3d71.setContent(html_18a364e67e704ee59bdd3e183bb5f972);
        

        marker_5cc11434e0e54457ab017b7bd5a3e490.bindPopup(popup_d5fb704f185548d1b96873092b2a3d71)
        ;

        
    
    
            var marker_b919f6ebb8fb4507b44eccaf4b45f2c5 = L.marker(
                [34.0008872704639, -84.5883881952453],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_329eb1afdfc344a282b9882513b13213 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_b919f6ebb8fb4507b44eccaf4b45f2c5.setIcon(icon_329eb1afdfc344a282b9882513b13213);
        
    
        var popup_0558200dd1b24a5cabe1de4bc8b7e3e0 = L.popup({"maxWidth": "100%"});

        
            var html_5b78a6130fe646d3a35a31b649bf2fc9 = $(`<div id="html_5b78a6130fe646d3a35a31b649bf2fc9" style="width: 100.0%; height: 100.0%;">Taj Mahal Grill</div>`)[0];
            popup_0558200dd1b24a5cabe1de4bc8b7e3e0.setContent(html_5b78a6130fe646d3a35a31b649bf2fc9);
        

        marker_b919f6ebb8fb4507b44eccaf4b45f2c5.bindPopup(popup_0558200dd1b24a5cabe1de4bc8b7e3e0)
        ;

        
    
    
            var marker_769fb62c6eac40619655aaaa53133142 = L.marker(
                [33.8566085797099, -84.38271659804009],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_a452daa7dd484467b7aa723b7dd11954 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_769fb62c6eac40619655aaaa53133142.setIcon(icon_a452daa7dd484467b7aa723b7dd11954);
        
    
        var popup_a7d00b8a9b50491a936a4561ee6f403d = L.popup({"maxWidth": "100%"});

        
            var html_1f342545d79f4eedac11864111667518 = $(`<div id="html_1f342545d79f4eedac11864111667518" style="width: 100.0%; height: 100.0%;">JINYA Ramen Bar</div>`)[0];
            popup_a7d00b8a9b50491a936a4561ee6f403d.setContent(html_1f342545d79f4eedac11864111667518);
        

        marker_769fb62c6eac40619655aaaa53133142.bindPopup(popup_a7d00b8a9b50491a936a4561ee6f403d)
        ;

        
    
    
            var marker_d5df20b741954372b2defb17e71bc1d7 = L.marker(
                [33.9475624005883, -84.33496600000001],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_4db6931e34d04e44b99ebef9de31decc = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_d5df20b741954372b2defb17e71bc1d7.setIcon(icon_4db6931e34d04e44b99ebef9de31decc);
        
    
        var popup_642890c268d14bc7a909212e657088e2 = L.popup({"maxWidth": "100%"});

        
            var html_b6479b0c11b946b88d7d99669178db5b = $(`<div id="html_b6479b0c11b946b88d7d99669178db5b" style="width: 100.0%; height: 100.0%;">NFA Burger</div>`)[0];
            popup_642890c268d14bc7a909212e657088e2.setContent(html_b6479b0c11b946b88d7d99669178db5b);
        

        marker_d5df20b741954372b2defb17e71bc1d7.bindPopup(popup_642890c268d14bc7a909212e657088e2)
        ;

        
    
    
            var marker_4b9a2fb0f9e54faf842d94c5657966cd = L.marker(
                [33.8986473470416, -84.44717852760309],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_be52db1c9cd144c388ac1acaf0766949 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_4b9a2fb0f9e54faf842d94c5657966cd.setIcon(icon_be52db1c9cd144c388ac1acaf0766949);
        
    
        var popup_4188bd31ba504c819e74dadc2332a5e1 = L.popup({"maxWidth": "100%"});

        
            var html_5b79eda3d42d4c7b94fbe16a30f7b731 = $(`<div id="html_5b79eda3d42d4c7b94fbe16a30f7b731" style="width: 100.0%; height: 100.0%;">Heirloom Market BBQ</div>`)[0];
            popup_4188bd31ba504c819e74dadc2332a5e1.setContent(html_5b79eda3d42d4c7b94fbe16a30f7b731);
        

        marker_4b9a2fb0f9e54faf842d94c5657966cd.bindPopup(popup_4188bd31ba504c819e74dadc2332a5e1)
        ;

        
    
    
            var marker_0ab158d469194fddabdb3c67d5db9c3d = L.marker(
                [33.9411734961952, -84.2125377030411],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_8531f8cfd38c4822827d7e13d788a381 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_0ab158d469194fddabdb3c67d5db9c3d.setIcon(icon_8531f8cfd38c4822827d7e13d788a381);
        
    
        var popup_3ca46abfd122418990b2da7ba2f32e06 = L.popup({"maxWidth": "100%"});

        
            var html_df58fe6a9747482a9de20369511790ff = $(`<div id="html_df58fe6a9747482a9de20369511790ff" style="width: 100.0%; height: 100.0%;">Bleu House</div>`)[0];
            popup_3ca46abfd122418990b2da7ba2f32e06.setContent(html_df58fe6a9747482a9de20369511790ff);
        

        marker_0ab158d469194fddabdb3c67d5db9c3d.bindPopup(popup_3ca46abfd122418990b2da7ba2f32e06)
        ;

        
    
    
            var marker_0846310494a7425589af12883125f677 = L.marker(
                [34.0403326, -84.34251529999999],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_95b51b43641242829c0505b01e19672f = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_0846310494a7425589af12883125f677.setIcon(icon_95b51b43641242829c0505b01e19672f);
        
    
        var popup_ae98475728e540ff85b238a064d10101 = L.popup({"maxWidth": "100%"});

        
            var html_85161270ffb245fa8bc412e8d23a2a51 = $(`<div id="html_85161270ffb245fa8bc412e8d23a2a51" style="width: 100.0%; height: 100.0%;">Jerusalem Chef Restaurant</div>`)[0];
            popup_ae98475728e540ff85b238a064d10101.setContent(html_85161270ffb245fa8bc412e8d23a2a51);
        

        marker_0846310494a7425589af12883125f677.bindPopup(popup_ae98475728e540ff85b238a064d10101)
        ;

        
    
    
            var marker_d41887bd5f4043a79fc5eaecef5d1b83 = L.marker(
                [33.9520084, -84.5488322],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_0a4bc551b406469a9e799e64ccc1cd24 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_d41887bd5f4043a79fc5eaecef5d1b83.setIcon(icon_0a4bc551b406469a9e799e64ccc1cd24);
        
    
        var popup_fc557c194fa744c5b9a06c29291e5adb = L.popup({"maxWidth": "100%"});

        
            var html_89df482af7ff4e7488134827e3a82adb = $(`<div id="html_89df482af7ff4e7488134827e3a82adb" style="width: 100.0%; height: 100.0%;">The Marietta Local</div>`)[0];
            popup_fc557c194fa744c5b9a06c29291e5adb.setContent(html_89df482af7ff4e7488134827e3a82adb);
        

        marker_d41887bd5f4043a79fc5eaecef5d1b83.bindPopup(popup_fc557c194fa744c5b9a06c29291e5adb)
        ;

        
    
    
            var marker_ebfe8662679e45369385076b54bf4a96 = L.marker(
                [34.0178225891952, -84.6195390075445],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_0d38e2014a3f45d5b7052a413c0ab274 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_ebfe8662679e45369385076b54bf4a96.setIcon(icon_0d38e2014a3f45d5b7052a413c0ab274);
        
    
        var popup_e7a2b7943b8c468b8b4a6c83256b6a24 = L.popup({"maxWidth": "100%"});

        
            var html_8535dc1099594236bb349db47fd48150 = $(`<div id="html_8535dc1099594236bb349db47fd48150" style="width: 100.0%; height: 100.0%;">Italia Mediterranean Grill</div>`)[0];
            popup_e7a2b7943b8c468b8b4a6c83256b6a24.setContent(html_8535dc1099594236bb349db47fd48150);
        

        marker_ebfe8662679e45369385076b54bf4a96.bindPopup(popup_e7a2b7943b8c468b8b4a6c83256b6a24)
        ;

        
    
    
            var marker_6b80420ad7294a2694c35325b34ff89d = L.marker(
                [33.8929143, -84.47794329999999],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_dc088f74fb834e7085afc2c6fb615431 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_6b80420ad7294a2694c35325b34ff89d.setIcon(icon_dc088f74fb834e7085afc2c6fb615431);
        
    
        var popup_339b0a938c4e4d949dbf48e4d83e79d5 = L.popup({"maxWidth": "100%"});

        
            var html_b2cd70b5739c499caf8f597eaf6d5e2f = $(`<div id="html_b2cd70b5739c499caf8f597eaf6d5e2f" style="width: 100.0%; height: 100.0%;">Tacos La Villa</div>`)[0];
            popup_339b0a938c4e4d949dbf48e4d83e79d5.setContent(html_b2cd70b5739c499caf8f597eaf6d5e2f);
        

        marker_6b80420ad7294a2694c35325b34ff89d.bindPopup(popup_339b0a938c4e4d949dbf48e4d83e79d5)
        ;

        
    
    
            var marker_60150ea6bd3643589ba9b0c1b603ce3f = L.marker(
                [34.02839, -84.65044],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_5bbca6aef04b476cbe3f4469cfd40b1d = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_60150ea6bd3643589ba9b0c1b603ce3f.setIcon(icon_5bbca6aef04b476cbe3f4469cfd40b1d);
        
    
        var popup_f310ca80e10a40a8843a3c2cb2e73216 = L.popup({"maxWidth": "100%"});

        
            var html_37e72446d71f4bd8adb2ed052c10af15 = $(`<div id="html_37e72446d71f4bd8adb2ed052c10af15" style="width: 100.0%; height: 100.0%;">Pita King</div>`)[0];
            popup_f310ca80e10a40a8843a3c2cb2e73216.setContent(html_37e72446d71f4bd8adb2ed052c10af15);
        

        marker_60150ea6bd3643589ba9b0c1b603ce3f.bindPopup(popup_f310ca80e10a40a8843a3c2cb2e73216)
        ;

        
    
    
            var marker_9c918bdab268440abd01ed642703e60b = L.marker(
                [33.867515000000004, -84.19169699999999],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_63316b0759714e078582fdcfc46880de = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_9c918bdab268440abd01ed642703e60b.setIcon(icon_63316b0759714e078582fdcfc46880de);
        
    
        var popup_3b891d239b7440219e958d819f22fcec = L.popup({"maxWidth": "100%"});

        
            var html_5eeaa206bcff4bb0a7b2ae6065f59518 = $(`<div id="html_5eeaa206bcff4bb0a7b2ae6065f59518" style="width: 100.0%; height: 100.0%;">Taqueria San Pancho</div>`)[0];
            popup_3b891d239b7440219e958d819f22fcec.setContent(html_5eeaa206bcff4bb0a7b2ae6065f59518);
        

        marker_9c918bdab268440abd01ed642703e60b.bindPopup(popup_3b891d239b7440219e958d819f22fcec)
        ;

        
    
    
            var marker_862d833617c24ad3b4fbf5a4af84ecca = L.marker(
                [34.0188297326194, -84.3117081666565],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_36472781bf084565b5754fd3c7bd46c4 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_862d833617c24ad3b4fbf5a4af84ecca.setIcon(icon_36472781bf084565b5754fd3c7bd46c4);
        
    
        var popup_c0b40b04291547479320c3ca57a26c37 = L.popup({"maxWidth": "100%"});

        
            var html_841e93a0c09340dd839253c278203615 = $(`<div id="html_841e93a0c09340dd839253c278203615" style="width: 100.0%; height: 100.0%;">Foundation Social Eatery</div>`)[0];
            popup_c0b40b04291547479320c3ca57a26c37.setContent(html_841e93a0c09340dd839253c278203615);
        

        marker_862d833617c24ad3b4fbf5a4af84ecca.bindPopup(popup_c0b40b04291547479320c3ca57a26c37)
        ;

        
    
    
            var marker_b60ed90861e44378ab4277f959f76cc1 = L.marker(
                [34.0136946869881, -84.5675291148193],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_69523654d7644e1aa00e3de6acfc3b31 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_b60ed90861e44378ab4277f959f76cc1.setIcon(icon_69523654d7644e1aa00e3de6acfc3b31);
        
    
        var popup_a0c5369db2bc43f1a24bb66f988a777a = L.popup({"maxWidth": "100%"});

        
            var html_d7dc2ddb0e3b497a868524d81a8bd8cf = $(`<div id="html_d7dc2ddb0e3b497a868524d81a8bd8cf" style="width: 100.0%; height: 100.0%;">The Rotisserie Shop</div>`)[0];
            popup_a0c5369db2bc43f1a24bb66f988a777a.setContent(html_d7dc2ddb0e3b497a868524d81a8bd8cf);
        

        marker_b60ed90861e44378ab4277f959f76cc1.bindPopup(popup_a0c5369db2bc43f1a24bb66f988a777a)
        ;

        
    
    
            var marker_d3c78965a3f84f16b3d46533b5d437a2 = L.marker(
                [34.0167198820803, -84.362401664257],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_e27fefbb4d874ec1a908a3246f5822b7 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_d3c78965a3f84f16b3d46533b5d437a2.setIcon(icon_e27fefbb4d874ec1a908a3246f5822b7);
        
    
        var popup_048e398d70cd4b53ba0d9d2f1d9f9533 = L.popup({"maxWidth": "100%"});

        
            var html_20351a7f22e94c939f77173706c706de = $(`<div id="html_20351a7f22e94c939f77173706c706de" style="width: 100.0%; height: 100.0%;">Chippers Pub</div>`)[0];
            popup_048e398d70cd4b53ba0d9d2f1d9f9533.setContent(html_20351a7f22e94c939f77173706c706de);
        

        marker_d3c78965a3f84f16b3d46533b5d437a2.bindPopup(popup_048e398d70cd4b53ba0d9d2f1d9f9533)
        ;

        
    
    
            var marker_5a8b72e1bad24e3e928636a015e710b0 = L.marker(
                [33.882797, -84.50488299999999],
                {"color": "green"}
            ).addTo(marker_cluster_beaa8b32db5a4249bca7c9fd5f2f5d1f);
        
    
            var icon_7c2c2c6548d04a4cac3f58d302c6b3b3 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "bolt", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_5a8b72e1bad24e3e928636a015e710b0.setIcon(icon_7c2c2c6548d04a4cac3f58d302c6b3b3);
        
    
        var popup_8e9dd96cf239418885355852400e345c = L.popup({"maxWidth": "100%"});

        
            var html_810da842db5943b8ab2af98087fef724 = $(`<div id="html_810da842db5943b8ab2af98087fef724" style="width: 100.0%; height: 100.0%;">Mezza Luna</div>`)[0];
            popup_8e9dd96cf239418885355852400e345c.setContent(html_810da842db5943b8ab2af98087fef724);
        

        marker_5a8b72e1bad24e3e928636a015e710b0.bindPopup(popup_8e9dd96cf239418885355852400e345c)
        ;

        
    
</script>
