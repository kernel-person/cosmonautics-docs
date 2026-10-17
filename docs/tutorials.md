# Interactive Tutorials

Cosmonautics tutorials teach complete systems through private, interactive scenes. Open the catalog with:

```text
/cosmo tutorial
```

Select a lesson in chat or start one directly with `/cosmo tutorial <tutorial-id>`. Use `/cosmo tutorial stop` to leave at any time.

The lessons, including Moon workshop, do not require an advancement unlock. The `spaceplugin.tutorial` permission is enabled for players by default.

## See a tutorial in action

<video controls preload="metadata" playsinline poster="../images/launch-site-tutorial-poster.jpg" class="wiki-video">
  <source src="../videos/launch-site-tutorial.mp4" type="video/mp4">
  Your browser does not support embedded video. You can <a href="../videos/launch-site-tutorial.mp4">download the Launch Site tutorial recording</a> instead.
</video>

*A short playthrough of the Launch Site lesson, from constructing the pad to previewing Artemis and its propellants.*

## Available lessons

### Launch Site

```text
/cosmo tutorial launch-site
```

Build the 10 × 10 Artemis pad, craft and place the Launch Controller, connect its supply chest and progress comparator, preview Artemis assembly, and learn how Rocket Fuel and Oxidizer prepare the vehicle for launch.

![The Launch Site tutorial prompting the player to open propellant recipes](images/tutorial-launch-site.jpg){ .wiki-shot loading=lazy }

*Glowing objects and in-world prompts lead the player through each interactive step.*

### Survive in Space

```text
/cosmo tutorial survive-space
```

View recipes for a sealed suit, Oxygen Canisters, and the EVA Harness. The lesson then demonstrates pressure loss through broken glass, resealing and oxygenating a habitat, reading a Pressure Gauge, and cycling an airlock without opening both doors together.

![The Survive in Space tutorial showing the Glass Space Helmet recipe](images/tutorial-survive-space.jpg){ .wiki-shot loading=lazy }

*Tutorial recipe windows are safe previews: click the output or close the window to continue.*

### Space Station

```text
/cosmo tutorial space-station
```

Follow a station-founding mission into orbit, dock with the new station, install solar panels, process ice and mineral asteroids, operate the automated collector and defensive machines, preview access settings, and return to Earth.

![The Space Station tutorial asking the player to split a medium asteroid](images/tutorial-space-station.jpg){ .wiki-shot loading=lazy }

*The Station lesson uses glowing targets to demonstrate asteroid processing and machinery.*

### Moon workshop

```text
/cosmo tutorial moon-workshop
```

Learn the complete Scrap-to-equipment route through five chapters:

1. Find Lunar Scrap in a secured colony loot-room chest.
2. Produce Hydrogen in a powered Station brewing stand.
3. Brew Lunar Alloy Solution and craft finished Lunar Alloy.
4. View both Solo and Duo rover recipes, placement, refuelling, and driving. Floating W/A/S/D prompts show forward movement, reversing, and steering.
5. Preview the Copper Gun, Rocket Launcher, their ammunition, and how their shots behave.

The lesson demonstrates the existing recipes without giving you real items or firing real weapons. Thruster Assembly and interplanetary travel are outside this released lesson. See [Exploring the Moon](moon.md#make-lunar-alloy) and [Lunar Rovers](rovers.md) for the written recipes and controls.

## Controls and interactions

- Follow action-bar narration and click glowing scene objects when prompted.
- Clicking a machine or crafting target opens its preview immediately. In brewing previews, click the ingredient or any of the three bottom bottles to advance; the protected battery slot does not advance the lesson.
- The Moon hydrogen demonstration needs one processing click; it does not make you repeat the batch.
- Use the chat controls to move between chapters, replay, or exit. Interaction boundaries advance directly to the next glowing target.
- A completed scene remains visible until you use its glowing finish target.
- Only one tutorial session runs for you at a time.

!!! info "Private and safe"
    Tutorial blocks, entities, inventories, recipes, machines, and items exist only in your client-side lesson. Tutorials do not alter real blocks, entities, inventories, player state, or gameplay state.
