<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Disaster Management in India: An Interactive Overview</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <!-- Chosen Palette: Warm Neutrals -->
    <!-- Application Structure Plan: A thematic, single-page dashboard structure was chosen over a linear report format to enhance user engagement and facilitate non-linear exploration. The structure includes: 1) A top navigation bar for quick access to key sections. 2) An 'Overview' section with at-a-glance statistics and a donut chart to provide immediate context. 3) An interactive 'Disaster Types' section with category filters, allowing users to explore the 32 disaster types without being overwhelmed by a long list. 4) A 'Management Framework' section that uses an interactive diagram for the DM cycle and info cards for the legal/policy aspects. This user-centric design breaks down dense information into digestible, interactive modules, empowering the user to learn by exploring rather than just reading. -->
    <!-- Visualization & Content Choices: 
        - Report Info: 5 categories of disasters. Goal: Show proportions. Viz/Method: Donut Chart. Interaction: Hover to see details. Justification: Instantly visualizes the distribution of disaster types. Library: Chart.js (Canvas).
        - Report Info: 32 specific disaster types. Goal: Organize and allow exploration. Viz/Method: Filterable content cards. Interaction: Click category buttons to filter displayed cards. Justification: Turns a static list into an interactive exploratory tool. Library: Vanilla JS + Tailwind CSS.
        - Report Info: The DM Cycle (Prevention, Mitigation, etc.). Goal: Explain a continuous process. Viz/Method: A circular flow diagram built with HTML/CSS. Interaction: Click on a stage to read its description. Justification: Visually represents the cyclical nature of DM, which is more intuitive than text. Library: Vanilla JS + Tailwind CSS.
        - Report Info: DM Act, NDMP, Key Agencies. Goal: Inform about the framework. Viz/Method: Tabbed content cards. Interaction: Click tabs to switch between policy, act, and agencies. Justification: Organizes detailed textual information into a compact, user-controlled interface. Library: Vanilla JS + Tailwind CSS.
    -->
    <!-- CONFIRMATION: NO SVG graphics used. NO Mermaid JS used. -->
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #FDFBF8;
            color: #3f3f46;
        }
        .nav-link {
            transition: color 0.3s ease, border-bottom-color 0.3s ease;
            border-bottom: 2px solid transparent;
        }
        .nav-link:hover, .nav-link.active {
            color: #c2410c;
            border-bottom-color: #c2410c;
        }
        .filter-btn {
            transition: all 0.3s ease;
        }
        .filter-btn.active {
            background-color: #c2410c;
            color: white;
            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
        }
        .disaster-card {
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            will-change: transform;
        }
        .disaster-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
        }
        .chart-container {
            position: relative;
            width: 100%;
            max-width: 400px;
            margin-left: auto;
            margin-right: auto;
            height: 300px;
            max-height: 400px;
        }
        @media (min-width: 768px) {
            .chart-container {
                height: 350px;
            }
        }
        .dm-cycle-step {
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .dm-cycle-step:hover, .dm-cycle-step.active {
            background-color: #ea580c;
            color: white;
            transform: scale(1.05);
        }
        .tab-btn {
            transition: all 0.3s ease;
        }
        .tab-btn.active {
            border-color: #c2410c;
            background-color: #fff7ed;
            color: #c2410c;
        }
    </style>
</head>
<body class="antialiased">

    <header class="bg-white/80 backdrop-blur-md sticky top-0 z-50 shadow-sm">
        <nav class="container mx-auto px-6 py-4 flex justify-between items-center">
            <h1 class="text-xl md:text-2xl font-bold text-orange-800">Disasters in India</h1>
            <div class="hidden md:flex space-x-8">
                <a href="#overview" class="nav-link text-gray-600 font-medium pb-1">Overview</a>
                <a href="#types" class="nav-link text-gray-600 font-medium pb-1">Disaster Types</a>
                <a href="#framework" class="nav-link text-gray-600 font-medium pb-1">Management Framework</a>
            </div>
            <div class="md:hidden">
                <select id="mobile-nav" class="border border-gray-300 rounded-md p-2 bg-white text-gray-700">
                    <option value="#overview">Overview</option>
                    <option value="#types">Disaster Types</option>
                    <option value="#framework">Management Framework</option>
                </select>
            </div>
        </nav>
    </header>

    <main class="container mx-auto px-6 py-12">
        <section id="overview" class="mb-20 text-center">
            <h2 class="text-3xl md:text-4xl font-bold text-gray-800 mb-4">India's Disaster Landscape: An Overview</h2>
            <p class="max-w-3xl mx-auto text-gray-600 mb-12">
                India's unique geo-climatic conditions make it vulnerable to a wide range of natural and man-made disasters. The High Power Committee on Disaster Management has identified 32 distinct types. This dashboard provides an interactive exploration of these hazards and the robust framework established to manage them.
            </p>
            <div class="grid md:grid-cols-2 gap-8 items-center">
                <div class="bg-white p-6 rounded-lg shadow-md border border-gray-200">
                    <h3 class="text-2xl font-semibold text-gray-700 mb-4">Disaster Categories Breakdown</h3>
                     <div class="chart-container">
                        <canvas id="disasterTypesChart"></canvas>
                    </div>
                </div>
                <div class="space-y-6 text-left">
                    <div class="bg-white p-6 rounded-lg shadow-md border border-gray-200">
                        <p class="text-5xl font-bold text-orange-600">68%</p>
                        <p class="text-lg text-gray-700 mt-2">of agricultural land is prone to drought, highlighting a significant environmental and economic vulnerability.</p>
                    </div>
                    <div class="bg-white p-6 rounded-lg shadow-md border border-gray-200">
                         <p class="text-5xl font-bold text-blue-600">7,516 km</p>
                        <p class="text-lg text-gray-700 mt-2">of coastline is exposed to nearly 10% of the world's tropical cyclones, a major threat to coastal communities.</p>
                    </div>
                     <div class="bg-white p-6 rounded-lg shadow-md border border-gray-200">
                         <p class="text-5xl font-bold text-red-600">4 Zones</p>
                        <p class="text-lg text-gray-700 mt-2">India is divided into four seismic zones, with the Himalayan region being particularly vulnerable to high-intensity earthquakes.</p>
                    </div>
                </div>
            </div>
        </section>

        <section id="types" class="mb-20">
            <h2 class="text-3xl md:text-4xl font-bold text-gray-800 text-center mb-4">Explore Disaster Types</h2>
            <p class="max-w-3xl mx-auto text-gray-600 mb-10 text-center">
                From floods to industrial accidents, India faces a complex array of hazards. Select a category below to filter and learn about the specific disasters identified by the national framework. This interactive list allows you to focus on the types of disasters that interest you most.
            </p>
            <div id="filter-container" class="flex flex-wrap justify-center gap-2 md:gap-4 mb-10">
                <button class="filter-btn active px-4 py-2 bg-white border border-gray-300 rounded-full text-sm font-medium text-gray-700 hover:bg-orange-100" data-filter="all">All Types (32)</button>
                <button class="filter-btn px-4 py-2 bg-white border border-gray-300 rounded-full text-sm font-medium text-gray-700 hover:bg-orange-100" data-filter="water">Water & Climate</button>
                <button class="filter-btn px-4 py-2 bg-white border border-gray-300 rounded-full text-sm font-medium text-gray-700 hover:bg-orange-100" data-filter="geological">Geological</button>
                <button class="filter-btn px-4 py-2 bg-white border border-gray-300 rounded-full text-sm font-medium text-gray-700 hover:bg-orange-100" data-filter="chemical">Chemical & Industrial</button>
                <button class="filter-btn px-4 py-2 bg-white border border-gray-300 rounded-full text-sm font-medium text-gray-700 hover:bg-orange-100" data-filter="accident">Accident-Related</button>
                <button class="filter-btn px-4 py-2 bg-white border border-gray-300 rounded-full text-sm font-medium text-gray-700 hover:bg-orange-100" data-filter="biological">Biological</button>
            </div>

            <div id="disaster-grid" class="grid sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            </div>
        </section>

        <section id="framework" class="mb-16">
            <h2 class="text-3xl md:text-4xl font-bold text-gray-800 text-center mb-4">India's Disaster Management Framework</h2>
            <p class="max-w-3xl mx-auto text-gray-600 mb-12 text-center">
                India has shifted from a reactive, relief-centric approach to a proactive and holistic one focused on prevention, mitigation, and preparedness. This framework is built upon a robust legal and policy structure. Explore the key components of this strategy below.
            </p>

            <div class="grid lg:grid-cols-2 gap-12 items-start">
                <div class="bg-white p-6 rounded-lg shadow-lg border border-gray-200">
                    <h3 class="text-2xl font-semibold text-gray-700 mb-6 text-center">The Disaster Management Cycle</h3>
                    <p class="text-center text-gray-600 mb-6">Disaster management is a continuous cycle of activities. Click on any step to learn more about its role in building a resilient nation.</p>
                    <div class="relative w-full aspect-square max-w-md mx-auto">
                        <div id="cycle-center-text" class="absolute inset-0 flex items-center justify-center p-8">
                            <div class="text-center">
                                <h4 class="font-bold text-lg text-orange-700 mb-2">Select a Step</h4>
                                <p class="text-sm text-gray-600">Learn about each phase of the integrated disaster management process.</p>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="bg-white p-6 rounded-lg shadow-lg border border-gray-200">
                    <h3 class="text-2xl font-semibold text-gray-700 mb-6 text-center">Policy & Legislation</h3>
                    <div class="border-b border-gray-200">
                        <nav class="-mb-px flex space-x-4" aria-label="Tabs">
                            <button class="tab-btn active whitespace-nowrap py-4 px-1 border-b-2 font-medium text-sm" data-tab="policy">National Policy</button>
                            <button class="tab-btn whitespace-nowrap py-4 px-1 border-b-2 font-medium text-sm border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300" data-tab="act">DM Act, 2005</button>
                            <button class="tab-btn whitespace-nowrap py-4 px-1 border-b-2 font-medium text-sm border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300" data-tab="agencies">Key Agencies</button>
                        </nav>
                    </div>
                    <div class="pt-6">
                        <div id="policy-content" class="tab-content space-y-4">
                            <h4 class="text-xl font-bold text-gray-800">Vision</h4>
                            <p class="text-gray-600">To build a safe and disaster-resilient India by developing a holistic, proactive, multi-disaster oriented, and technology-driven strategy.</p>
                             <h4 class="text-xl font-bold text-gray-800">Core Objectives</h4>
                            <ul class="list-disc list-inside text-gray-600 space-y-2">
                                <li>Promote a culture of prevention, preparedness, and resilience.</li>
                                <li>Encourage mitigation measures based on technology and traditional wisdom.</li>
                                <li>Mainstream disaster management into development planning.</li>
                                <li>Ensure efficient response and relief, especially for vulnerable sections.</li>
                            </ul>
                        </div>
                        <div id="act-content" class="tab-content hidden space-y-4">
                            <h4 class="text-xl font-bold text-gray-800">Purpose</h4>
                            <p class="text-gray-600">Provides the institutional and legal framework for disaster management across India, establishing a clear chain of command.</p>
                             <h4 class="text-xl font-bold text-gray-800">Institutional Structure</h4>
                            <ul class="list-disc list-inside text-gray-600 space-y-2">
                                <li><strong>National Disaster Management Authority (NDMA):</strong> Chaired by the Prime Minister. Lays down policies, plans, and guidelines.</li>
                                <li><strong>State Disaster Management Authority (SDMA):</strong> Chaired by the Chief Minister.</li>
                                <li><strong>District Disaster Management Authority (DDMA):</strong> Headed by the District Collector.</li>
                            </ul>
                        </div>
                        <div id="agencies-content" class="tab-content hidden space-y-4">
                            <h4 class="text-xl font-bold text-gray-800">Primary Responsibility</h4>
                            <p class="text-gray-600">While States have the primary responsibility, the Central Government provides logistical and financial support.</p>
                             <h4 class="text-xl font-bold text-gray-800">Key National Bodies</h4>
                            <ul class="list-disc list-inside text-gray-600 space-y-2">
                                <li><strong>Ministry of Home Affairs (DM Division):</strong> Coordinates all central government efforts for disaster risk reduction.</li>
                                <li><strong>National Disaster Response Force (NDRF):</strong> A specialized force for responding to disaster situations.</li>
                                <li><strong>National Institute of Disaster Management (NIDM):</strong> Focuses on training, research, and capacity development.</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>
    
    <footer class="bg-gray-800 text-white mt-12">
        <div class="container mx-auto px-6 py-4 text-center">
            <p>An Interactive Dashboard on Disaster Management in India.</p>
        </div>
    </footer>


<script>
document.addEventListener('DOMContentLoaded', function() {
    const disasterData = [
        { name: 'Floods & Drainage', category: 'water', description: 'Caused by heavy rainfall and inadequate river capacity, a major issue in most river basins.' },
        { name: 'Cyclones', category: 'water', description: 'Tropical storms affecting India\'s long coastline with severe winds, rain, and storm surges.' },
        { name: 'Droughts', category: 'water', description: 'Caused by deficient rainfall, affecting vast agricultural areas and water supplies.' },
        { name: 'Tornadoes & Hurricanes', category: 'water', description: 'Violent rotating columns of air causing localized, intense damage.' },
        { name: 'Hailstorms', category: 'water', description: 'Precipitation in the form of ice, damaging crops and property.' },
        { name: 'Cloud Burst', category: 'water', description: 'An extreme amount of precipitation in a short period of time.' },
        { name: 'Heat & Cold Wave', category: 'water', description: 'Periods of abnormally hot or cold weather that can have severe public health impacts.' },
        { name: 'Snow Avalanches', category: 'water', description: 'Rapid flow of snow down a slope, a major hazard in Himalayan regions.' },
        { name: 'Sea Erosion', category: 'water', description: 'The wearing away of coastal land by sea action.' },
        { name: 'Thunder & Lightning', category: 'water', description: 'Electrical storms that can cause fires, deaths, and power outages.' },
        { name: 'Tsunami', category: 'water', description: 'Series of large ocean waves generated by undersea earthquakes or landslides.' },
        { name: 'Landslides & Mudflows', category: 'geological', description: 'Down-slope movement of rock, debris, or earth, common in Himalayan and Ghat regions.' },
        { name: 'Earthquakes', category: 'geological', description: 'Sudden shaking of the ground caused by seismic waves, with high risk in Himalayan areas.' },
        { name: 'Dam Failure / Bursts', category: 'geological', description: 'Catastrophic failure of a dam structure leading to downstream flooding.' },
        { name: 'Mine Disasters', category: 'geological', description: 'Accidents occurring in mines, including collapses, floods, and explosions.' },
        { name: 'Chemical & Industrial', category: 'chemical', description: 'Disasters from process failures, spills, or explosions at industrial plants.' },
        { name: 'Nuclear Disasters', category: 'chemical', description: 'Accidents at nuclear facilities leading to the release of radioactive material.' },
        { name: 'Forest Fires', category: 'accident', description: 'Uncontrolled fires in forests, posing a threat to flora, fauna, and human settlements.' },
        { name: 'Urban Fires', category: 'accident', description: 'Major fires in urban areas, including residential and commercial buildings.' },
        { name: 'Mine Flooding', category: 'accident', description: 'Inundation of underground mines with water, trapping miners.' },
        { name: 'Oil Spills', category: 'accident', description: 'Release of liquid petroleum hydrocarbon into the environment, causing ecological damage.' },
        { name: 'Major Building Collapse', category: 'accident', description: 'Structural failure of large buildings, often in urban areas.' },
        { name: 'Serial Bomb Blasts', category: 'accident', description: 'A series of coordinated terrorist bombings.' },
        { name: 'Festival Related Disasters', category: 'accident', description: 'Accidents such as stampedes or fires occurring during large festive gatherings.' },
        { name: 'Electrical Disasters', category: 'accident', description: 'Major accidents caused by electrical failures or short circuits.' },
        { name: 'Air, Road & Rail Accidents', category: 'accident', description: 'Large-scale transportation accidents resulting in significant casualties.' },
        { name: 'Boat Capsizing', category: 'accident', description: 'Overturning of boats, often due to overcrowding or bad weather.' },
        { name: 'Village Fire', category: 'accident', description: 'Fires that spread through rural villages, often with flammable housing materials.' },
        { name: 'Biological Disasters', category: 'biological', description: 'Outbreaks of infectious diseases like epidemics and pandemics.' },
        { name: 'Pest Attacks', category: 'biological', description: 'Widespread crop destruction caused by insects or other pests, like locust swarms.' },
        { name: 'Cattle Epidemics', category: 'biological', description: 'Widespread disease outbreaks among livestock, such as foot-and-mouth disease.' },
        { name: 'Food Poisoning', category: 'biological', description: 'Mass incidents of illness caused by consumption of contaminated food.' }
    ];

    const disasterGrid = document.getElementById('disaster-grid');
    const filterContainer = document.getElementById('filter-container');
    const filterButtons = filterContainer.querySelectorAll('.filter-btn');

    function displayDisasters(filter) {
        disasterGrid.innerHTML = '';
        const filteredData = filter === 'all' ? disasterData : disasterData.filter(d => d.category === filter);

        filteredData.forEach(disaster => {
            const card = document.createElement('div');
            card.className = 'disaster-card bg-white p-5 rounded-lg shadow-md border border-gray-200';
            card.innerHTML = `
                <h3 class="font-bold text-lg text-gray-800 mb-2">${disaster.name}</h3>
                <p class="text-gray-600 text-sm">${disaster.description}</p>
            `;
            disasterGrid.appendChild(card);
        });
    }

    filterContainer.addEventListener('click', (e) => {
        if (e.target.classList.contains('filter-btn')) {
            filterButtons.forEach(btn => btn.classList.remove('active'));
            e.target.classList.add('active');
            const filter = e.target.dataset.filter;
            displayDisasters(filter);
        }
    });

    displayDisasters('all');

    const ctx = document.getElementById('disasterTypesChart').getContext('2d');
    const chart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Water & Climate', 'Geological', 'Chemical & Industrial', 'Accident-Related', 'Biological'],
            datasets: [{
                label: 'Number of Disaster Types',
                data: [11, 4, 2, 11, 4],
                backgroundColor: [
                    'rgba(59, 130, 246, 0.7)',
                    'rgba(139, 92, 246, 0.7)',
                    'rgba(239, 68, 68, 0.7)',
                    'rgba(249, 115, 22, 0.7)',
                    'rgba(16, 185, 129, 0.7)'
                ],
                borderColor: [
                    'rgba(59, 130, 246, 1)',
                    'rgba(139, 92, 246, 1)',
                    'rgba(239, 68, 68, 1)',
                    'rgba(249, 115, 22, 1)',
                    'rgba(16, 185, 129, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom',
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            let label = context.label || '';
                            if (label) {
                                label += ': ';
                            }
                            if (context.parsed !== null) {
                                label += context.parsed + ' types';
                            }
                            return label;
                        }
                    }
                }
            }
        }
    });

    const cycleStepsData = [
        { name: 'Prevention', description: 'Measures to avoid the occurrence of a disaster altogether or to reduce its potential impact.' },
        { name: 'Mitigation', description: 'Actions taken to reduce the severity or consequences of a disaster, such as building codes and zoning.' },
        { name: 'Preparedness', description: 'Planning, training, and educational activities for events that cannot be mitigated.' },
        { name: 'Response', description: 'Actions taken immediately before, during, or directly after a disaster to save lives and meet basic human needs.' },
        { name: 'Rehabilitation', description: 'Actions to restore affected communities to their proper, pre-disaster level of functioning.' },
        { name: 'Reconstruction', description: 'The process of rebuilding communities, including "building back better" to be more resilient.' }
    ];
    
    const cycleCenter = document.getElementById('cycle-center-text');
    const cycleContainer = cycleCenter.parentElement;

    const radius = cycleContainer.offsetWidth / 2.5;
    const centerX = cycleContainer.offsetWidth / 2;
    const centerY = cycleContainer.offsetHeight / 2;
    const angleStep = (2 * Math.PI) / cycleStepsData.length;

    cycleStepsData.forEach((step, index) => {
        const angle = angleStep * index - (Math.PI / 2);
        const x = centerX + radius * Math.cos(angle) - 40;
        const y = centerY + radius * Math.sin(angle) - 40;

        const step_el = document.createElement('div');
        step_el.className = 'dm-cycle-step absolute flex items-center justify-center w-24 h-24 rounded-full bg-orange-500 text-white font-semibold text-center text-sm p-2 shadow-lg';
        step_el.style.left = `${x}px`;
        step_el.style.top = `${y}px`;
        step_el.textContent = step.name;
        step_el.dataset.description = step.description;
        cycleContainer.appendChild(step_el);

        step_el.addEventListener('click', () => {
            cycleContainer.querySelectorAll('.dm-cycle-step').forEach(el => el.classList.remove('active'));
            step_el.classList.add('active');
            cycleCenter.innerHTML = `
                <div class="text-center transition-opacity duration-300">
                    <h4 class="font-bold text-lg text-orange-700 mb-2">${step.name}</h4>
                    <p class="text-sm text-gray-600">${step.description}</p>
                </div>
            `;
        });
    });

    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');
    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            tabButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
            const tabId = button.dataset.tab;
            tabContents.forEach(content => {
                if (content.id === `${tabId}-content`) {
                    content.classList.remove('hidden');
                } else {
                    content.classList.add('hidden');
                }
            });
        });
    });

    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('section');
    
    window.addEventListener('scroll', () => {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            if (pageYOffset >= sectionTop - 100) {
                current = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });
    });
    
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    const mobileNav = document.getElementById('mobile-nav');
    mobileNav.addEventListener('change', (e) => {
        const targetId = e.target.value;
        document.querySelector(targetId).scrollIntoView({ behavior: 'smooth' });
    });

});
</script>

</body>
</html>
