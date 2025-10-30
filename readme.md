# Kev the Annoyer – 3D Destruction Simulation in Three.js

This project is a **lightweight, browser-based 3D destruction animation** inspired by the cinematic short featuring "Kev the Annoyer," a starfish-like character based on Starro the Conqueror from *Suicide Squad*. The original workflow used Blender and Houdini for modeling, rigging, animation, and destruction simulation. This implementation recreates a **stylized, interactive version entirely in Three.js**, suitable for web AR/VR demonstrations.

---

## 🚀 Quick Start

### Option 1: Direct Browser (Simplest)
1. Open `index.html` directly in a modern browser
2. Click "SMASH!" or press SPACE to trigger destruction
3. Use mouse to orbit the camera

### Option 2: Local Server (Recommended for WebXR)
```bash
# Using Python (built-in)
python server.py

# Or using Node.js
npm install
npm run serve
```

### Option 3: Live Server Extension
If using VS Code, install "Live Server" extension and right-click `index.html` → "Open with Live Server"

---

## 🎮 Controls

- **Mouse**: Orbit camera around the scene
- **SPACE** or **SMASH! button**: Trigger destruction animation
- **Reset button**: Reset the scene to initial state
- **Enter VR button**: Launch WebXR VR mode (if supported)

---

## 🥽 VR/AR Support

### VR Requirements
- WebXR compatible browser (Chrome 79+, Edge 79+)
- VR headset (Oculus, HTC Vive, Windows Mixed Reality, etc.)
- Serve over HTTPS or localhost

### AR Requirements (Future Enhancement)
- Chrome on Android with ARCore support
- WebXR AR implementation (can be added)

---

## 📁 File Structure

```
arvr/
├── index.html          # Main application file
├── new.html            # Original prototype
├── server.py           # Python development server
├── package.json        # Node.js dependencies
└── README.md           # This file
```

---

## 🔧 Implementation Details

### Core Features Implemented
✓ **Procedural Starfish Model**: 5-limb starfish with animated breathing and limb movement
✓ **Physics-Based Destruction**: Real-time building collapse using Cannon-es physics
✓ **Particle Effects**: Explosion debris and smoke simulation
✓ **Smooth Animation**: GSAP-powered character movement and camera effects
✓ **WebXR VR Support**: Compatible with VR headsets via WebXR API
✓ **Interactive Controls**: Mouse orbit, keyboard shortcuts, UI buttons
✓ **Responsive Design**: Adapts to different screen sizes

### Technical Stack Used
- **Three.js 0.158.0**: 3D graphics and rendering
- **Cannon-es 0.20.0**: Physics simulation
- **GSAP 3.12.2**: Smooth animations
- **WebXR**: VR/AR support
- **Vanilla JavaScript**: No framework dependencies

---

## 🎆 Features in Action

1. **Character Animation**: Kev breathes, floats, and moves his limbs naturally
2. **Physics Destruction**: Building blocks react realistically to impact
3. **Particle System**: Explosion creates debris that falls with gravity
4. **Camera Effects**: Screen shake and smooth transitions enhance impact
5. **VR Mode**: Full 6DOF experience in compatible VR headsets

---

## ⚡ Tech Stack
| Component | Library / Tool |
|-----------|----------------|
| 3D Graphics | [Three.js](https://threejs.org/) |
| Physics | [Cannon-es](https://github.com/pmndrs/cannon-es) |
| Animation | [GSAP](https://greensock.com/gsap/) |
| Particles / Smoke | Three.js Points / ShaderMaterial |
| AR/VR | WebXR / Three.js VRButton |
| Deployment | Browser-based (works on GitHub Pages, Netlify, or localhost) |

---

## 🕰️ Performance Notes

- Optimized for 60fps on modern browsers
- Physics simulation limited to ~128 rigid bodies for performance
- Particle count automatically managed to prevent frame drops
- Shadow mapping enabled for realistic lighting
- Works on mobile devices (touch controls for camera)

---

## 🔮 Future Enhancements

- [ ] WebXR AR mode for mobile devices
- [ ] Sound effects and spatial audio
- [ ] Multiple building types and destruction patterns
- [ ] Multiplayer support via WebRTC
- [ ] Advanced particle shaders for better smoke/fire effects
- [ ] Hand tracking for VR interaction

---

## 📝 License

MIT License - Feel free to use this project for learning, modification, or commercial purposes.

---

**Built with ❤️ for the web platform**