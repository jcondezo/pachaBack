from orator.migrations import Migration


class CreateProfesoresTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('profesores') as table:
            table.increments('id')
            table.string('nombre')
            table.string('apellido')
            table.string('correo').unique()
            table.string('password')
            table.integer('salon_id').unsigned()
            table.foreign('salon_id').references('id').on('salones')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('profesores')
