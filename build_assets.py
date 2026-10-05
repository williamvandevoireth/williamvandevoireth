import textwrap
from xml.sax.saxutils import escape as e

W = 900
FONT = "'Helvetica Neue', Helvetica, Arial, sans-serif"

def panel(name, title, items):
    y = 84
    out = []
    for kind, *a in items:
        if kind == "p":
            for l in textwrap.wrap(a[0], 80):
                out.append(f'<text x="64" y="{y}" fill="#D1D5DB" font-size="19">{e(l)}</text>'); y += 29
            y += 2
        elif kind == "h":
            out.append(f'<text x="64" y="{y}" fill="#FFFFFF" font-size="21" font-weight="700">{e(a[0])}</text>')
            if len(a) > 1:
                out.append(f'<text x="{W-40}" y="{y}" fill="#E10600" font-size="14" font-weight="700" letter-spacing="1" text-anchor="end">{e(a[1])}</text>')
            y += 27
            if len(a) > 2:
                out.append(f'<text x="64" y="{y}" fill="#9CA3AF" font-size="17">{e(a[2])}</text>'); y += 28
        elif kind == "b":
            for i, l in enumerate(textwrap.wrap(a[0], 76)):
                if i == 0:
                    out.append(f'<rect x="64" y="{y-7}" width="8" height="3" fill="#E10600"/>')
                out.append(f'<text x="86" y="{y}" fill="#D1D5DB" font-size="18">{e(l)}</text>'); y += 26
        elif kind == "row":
            out.append(f'<text x="64" y="{y}" fill="#E10600" font-size="14" font-weight="700" letter-spacing="1">{e(a[0].upper())}</text>')
            out.append(f'<text x="64" y="{y+24}" fill="#D1D5DB" font-size="18">{e(a[1])}</text>'); y += 58
        elif kind == "gap":
            y += 12
    H = y + 4
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{e(title)}">
<defs><pattern id="c" width="8" height="8" patternUnits="userSpaceOnUse"><path d="M0 8L8 0" stroke="#fff" stroke-opacity="0.035"/></pattern>
<linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0B0B0D"/><stop offset="1" stop-color="#17181C"/></linearGradient></defs>
<g font-family="{FONT}">
<rect width="{W}" height="{H}" fill="url(#g)"/><rect width="{W}" height="{H}" fill="url(#c)"/>
<rect x="0" y="0" width="6" height="{H}" fill="#E10600"><animate attributeName="height" from="0" to="{H}" dur="0.9s" fill="freeze"/></rect>
<text x="64" y="46" fill="#FFFFFF" font-size="16" font-weight="700" letter-spacing="4">{e(title.upper())}</text>
<rect x="64" y="58" width="56" height="2" fill="#E10600"/>
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
    ("b", "Photovoltaic layout optimization"),
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
    ("h", "PV Layout Optimization (ss_solar_sim)"),
    ("b", "Bypass-diode dynamic programming, simulated annealing and string-length sweeps.")])
panel("skills", "Technical Skills", [
    ("row", "Control & Modelling", "FOC, MPC / QP control, MATLAB / Simulink, PV simulation"),
    ("row", "Embedded", "C / C++, CAN, microcontrollers, RTOS"),
    ("row", "Software", "Python, ROS, Docker, Git, Linux, LaTeX"),
    ("row", "Mechanical", "CAD (NX), Abaqus FEA, LabVIEW")])
