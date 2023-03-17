use std::process::Command;

fn main() {
    Command::new("py").arg("main.py").spawn().expect("Failed to run game");
}
