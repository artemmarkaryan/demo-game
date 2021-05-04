namespace DemoGame.domain.units {
public interface IUnit {
	int Id { get; }
	string Name { get; }
	int HitPoints { get; }
	int Attack { get; }
	int Defence { get; }
	int Cost { get;  }
	bool Cloneable { get; }

	// С какой вер-ю сработает спецдействие
	double SpecialActionProbability { get; }
	// Спецдействие
	void SpecialAction(Army friends, Army enemies) {
	}
}
}