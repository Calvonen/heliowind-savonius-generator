$fn = 180;

height = 460;
radius = 110;
plate_radius = 150;
plate_thickness = 6;
shaft_radius = 6;

blade_width = 95;
blade_thickness = 1.5;
twist_angle = 180;
slices = 200;

module blade(angle=0) {
    rotate([0,0,angle])
    linear_extrude(
        height = height,
        twist = twist_angle,
        slices = slices,
        convexity = 10
    )
    translate([radius + 10,0,0])
    rotate([0,0,90])
    offset(r=6)
    square([blade_width, blade_thickness], center=true);
}

module plate(z=0) {
    translate([0,0,z])
    difference() {
        cylinder(h=plate_thickness, r=plate_radius);
        cylinder(h=plate_thickness+1, r=shaft_radius);
    }
}

blade(0);
blade(180);

plate(0);
plate(height);

cylinder(h=height, r=shaft_radius);