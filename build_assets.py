import textwrap
from xml.sax.saxutils import escape as e

W = 1200
FONT = "'Helvetica Neue', Helvetica, Arial, sans-serif"

def panel(name, title, items):
    y = 78
    out = []
    for kind, *a in items:
        if kind == "p":
            for l in textwrap.wrap(a[0], 118):
                out.append(f'<text x="64" y="{y}" fill="#D1D5DB" font-size="16">{e(l)}</text>'); y += 26
            y += 6
        elif kind == "h":
            out.append(f'<text x="64" y="{y}" fill="#FFFFFF" font-size="17" font-weight="700">{e(a[0])}</text>')
            if len(a) > 1:
                out.append(f'<text x="1136" y="{y}" fill="#9CA3AF" font-size="13" letter-spacing="1" text-anchor="end">{e(a[1])}</text>')
            y += 24
            if len(a) > 2:
                out.append(f'<text x="64" y="{y}" fill="#9CA3AF" font-size="14">{e(a[2])}</text>'); y += 24
        elif kind == "b":
            for i, l in enumerate(textwrap.wrap(a[0], 112)):
                if i == 0:
                    out.append(f'<rect x="64" y="{y-9}" width="6" height="2" fill="#E10600"/>')
                out.append(f'<text x="82" y="{y}" fill="#D1D5DB" font-size="15">{e(l)}</text>'); y += 22
        elif kind == "row":
            out.append(f'<text x="64" y="{y}" fill="#E10600" font-size="12" font-weight="700" letter-spacing="2">{e(a[0].upper())}</text>')
            out.append(f'<text x="260" y="{y}" fill="#D1D5DB" font-size="15">{e(a[1])}</text>'); y += 30
        elif kind == "gap":
            y += 14
    H = y + 12
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{e(title)}">
<defs><pattern id="c" width="8" height="8" patternUnits="userSpaceOnUse"><path d="M0 8L8 0" stroke="#fff" stroke-opacity="0.035"/></pattern>
<linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0B0B0D"/><stop offset="1" stop-color="#17181C"/></linearGradient></defs>
<g font-family="{FONT}">
<rect width="{W}" height="{H}" fill="url(#g)"/><rect width="{W}" height="{H}" fill="url(#c)"/>
<rect x="0" y="0" width="6" height="{H}" fill="#E10600"><animate attributeName="height" from="0" to="{H}" dur="0.9s" fill="freeze"/></rect>
<text x="64" y="44" fill="#FFFFFF" font-size="13" font-weight="700" letter-spacing="5">{e(title.upper())}</text>
<rect x="64" y="54" width="48" height="2" fill="#E10600"/>
{chr(10).join(out)}
</g></svg>'''
    open(f"assets/{name}.svg", "w").write(svg)

panel("about", "About", [("p", "Mechanical engineering student at ETH Zürich specialising in control systems and robotics. My work focuses on motor control and drivetrain design for electric vehicles, optimization-based vehicle control, and photovoltaic system modelling and simulation.")])
panel("education", "Education", [
    ("h", "MSc Mechanical Engineering, Control Systems", "FEB 2026 – PRESENT", "ETH Zürich"), ("gap",),
    ("h", "BSc Mechanical Engineering, Robotics & Control", "SEP 2022 – FEB 2026", "ETH Zürich")])
panel("experience", "Experience", [
    ("h", "Drivetrain and Control Systems Engineer", "OCT 2025 – PRESENT", "aCentauri Solar Racing"),
    ("b", "Inverter and motor control: field-oriented control (FOC) in Simulink, sensorless PMSM, embedded C on PSoC C3, CAN communication"),
    ("b", "Photovoltaic string optimisation and MPPT modelling"),
    ("b", "Targets: 2026 European Solar Challenge, 2027 World Solar Challenge"), ("gap",),
    ("h", "Bachelor Thesis", "OCT 2025 – FEB 2026", "AMZ Racing Formula Student, ETH Zürich"),
    ("b", "Optimization-Based Torque Vectoring: real-time QP controller for yaw-rate tracking and tire utilisation"),
    ("b", "Supervisors: Prof. M. Zeilinger, Dr. A. Carron  ·  Grade: 5.75 / 6.0"), ("gap",),
    ("h", "Structural Engineer", "SEP 2023 – DEC 2024", "ARIS Rockets, Project Nicollier"),
    ("b", "3000 m apogee sounding rocket, two launches"),
    ("b", "Airbrake system CAD; composite manufacturing of fins, nosecone and fairing"), ("gap",),
    ("h", "Teaching Assistant", "SEP – DEC 2024", "ETH Zürich"),
    ("b", "Engineering Design and Material Selection: CAD, technical drawing, additive manufacturing")])
panel("projects", "Selected Projects", [
    ("h", "Traction Inverter, aCentauri Solar Racing"),
    ("b", "Simulink-based FOC with speed and torque control loops and CAN interface. 138 V DC bus, 40 A peak, PSoC C3."), ("gap",),
    ("h", "PV String Optimisation (ss_solar_sim)"),
    ("b", "Bypass-diode dynamic programming, simulated annealing, string-length sweeps and an MPPT model.")])
panel("skills", "Technical Skills", [
    ("row", "Control & Modelling", "Field-oriented control, MPC / QP-based control, MATLAB / Simulink, PV simulation"),
    ("row", "Embedded", "C / C++, CAN, microcontrollers, RTOS"),
    ("row", "Software", "Python, ROS, Docker, Git, Linux, LaTeX"),
    ("row", "Mechanical", "CAD (NX), Abaqus FEA, LabVIEW")])
